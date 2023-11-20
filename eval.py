import json
import zhconv
import Levenshtein
import numpy as np
import argparse

from shapely.geometry import Polygon, MultiPoint


def polyIoU(box1, box2):
    box1 = np.array(box1).reshape(4, 2)
    box2 = np.array(box2).reshape(4, 2)
    union_poly = np.concatenate((box1, box2))
    box1 = Polygon(box1).convex_hull
    box2 = Polygon(box2).convex_hull

    if not box1.intersects(box2):
        iou = 0
    else:
        inter_area = box1.intersection(box2).area
        union_area = MultiPoint(union_poly).convex_hull.area
        if union_area == 0:
            return 0
        iou = float(inter_area) / union_area
    return iou


def is_chinese_question(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


def process_ans(ans):
    ans = ans.lower()
    ans = zhconv.convert(ans, 'zh-cn')  # convert possible traditional annos to simplified
    return ans


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--gt_path', type=str, default='./gt_sample.json')
    argparser.add_argument('--pred_path', type=str, default='./pred_sample.json')
    args = argparser.parse_args()
    output = {}
    CLC_bi, LC_bi, TC_bi, CLC_en, LC_en, TC_en, CLC_ch, LC_ch, TC_ch = [], [], [], [], [], [], [], [], []

    with open(args.gt_path, 'r') as f:
        gts = json.load(f)
    with open(args.pred_path, 'r') as f:
        preds = json.load(f)

    assert len(gts) == len(preds)

    for gt, pred in zip(gts, preds):
        assert gt['question_id'] == pred['question_id']

        gt_ans = process_ans(gt['answer'])
        gt_evidence = list(map(int, gt['evidence']))
        pred_ans = process_ans(pred['answer'])
        pred_evidence = list(map(int, pred['evidence']))

        NL = Levenshtein.distance(gt_ans, pred_ans) / max(len(gt_ans), len(pred_ans))
        TC_SCORE = 1 - NL if NL < 0.5 else 0
        LC_score = polyIoU(gt_evidence, pred_evidence)
        CLC_score = TC_SCORE if LC_score >= 0.5 else 0

        CLC_bi.append(CLC_score)
        LC_bi.append(LC_score)
        TC_bi.append(TC_SCORE)

        if is_chinese_question(gt['question']):
            CLC_ch.append(CLC_score)
            LC_ch.append(LC_score)
            TC_ch.append(TC_SCORE)
        else:
            CLC_en.append(CLC_score)
            LC_en.append(LC_score)
            TC_en.append(TC_SCORE)

    output["result"] = [
        {
            "test_split": {
                "CLC": np.mean(CLC_bi),
                # "CLC_en": np.mean(CLC_en),
                # "CLC_ch": np.mean(CLC_ch),
                # "LC": np.mean(LC_bi),
                # "LC_en": np.mean(LC_en),
                # "LC_ch": np.mean(LC_ch),
                # "TC": np.mean(TC_bi),
                # "TC_en": np.mean(TC_en),
                # "TC_ch": np.mean(TC_ch),
            }
        }
    ]

    print(output)
