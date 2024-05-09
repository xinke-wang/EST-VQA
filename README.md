# On the General Value of Evidence, and Bilingual Scene-Text Visual Question Answering

<a href='https://openaccess.thecvf.com/content_CVPR_2020/papers/Wang_On_the_General_Value_of_Evidence_and_Bilingual_Scene-Text_Visual_CVPR_2020_paper.pdf'><img src='https://img.shields.io/badge/Paper-PDF-orange'></a>

Since the host server of EST-VQA dataset is no longer available, we provide the download link of the dataset in this repository.

We also release the test annotation here, so you don't have to use the EvalAI for evaluation now.

## Download

Google Drive: \[[Images Train](https://drive.google.com/file/d/15q8Hqx3uQm8mx4w3PZtactJVe1BRXug5/view)\] \[[Images Test](https://drive.google.com/file/d/1oP7dkEApOaU1I0QvJbvl0gDCM_ig5Vgb/view)\] \[[Annotations Train](https://drive.google.com/file/d/1M3fWhFWltjM_nFR0ALynUIwXatwKXb26/view)\] \[[Annotations Test](https://drive.google.com/file/d/1NUW2GJhqlpOmNEGic7_4wClzCIUH0NPW/view)\]

Baidu Netdisk: \[[Images](https://pan.baidu.com/s/1QsTZSrRwQcT4A2Vp2cR8GA?pwd=dcmn)\](code: dcmn) \[[Annotations](https://pan.baidu.com/s/15s8OZsIXhPuWQSCBXbQRNg?pwd=e4qe)\](code:e4qe)


## Evaluation

You can use `eval.py` to evaluate your model on EST-VQA dataset. Simply convert your prediction file to the same format as `pred_sample.json` and run the following command:

```
python eval.py --pred_file PATH_TO_PRED --gt_file PATH_TO_GT
```

## Leaderboard

Part of the results is borrowed from this [paper](https://arxiv.org/pdf/2305.07895).

| Year | Venue   | Model          | LLM-based | EST-VQA (En) | EST-VQA (CN) | Overall |
|------|---------|----------------|-----------|--------------|--------------|---------|
| 2023 | ICML    | [BLIP2-OPT-6.7B](https://github.com/salesforce/LAVIS/tree/main/projects/blip2) | Y         | 40.7         | 0            |         |
| 2023 | NeurIPS | [InstructBlip](https://github.com/salesforce/LAVIS/tree/main/projects/instructblip)   | Y         | 48.6         | 0.1          |         |
| 2023 | arxiv   | [mPlug-Owl](https://github.com/X-PLUG/mPLUG-Owl/tree/main/mPLUG-Owl)      | Y         | 52.7         | 0            |         |
| 2023 | arxiv   | [LLaVAR](https://github.com/SALT-NLP/LLaVAR)         | Y         | 58.2         | 0            |         |
| 2023 | NeurIPS   | [LLaVA-1.5-7B](https://github.com/haotian-liu/LLaVA)   | Y         | 52.3         | 0            |         |
| 2024 | AAAI    | [BLIVA](https://github.com/mlpc-ucsd/BLIVA)          | Y         | 51.2         | 0.2          |         |
| 2024 | CVPR    | [mPLUG-Owl2](https://github.com/X-PLUG/mPLUG-Owl/tree/main/mPLUG-Owl2)     | Y         | 68.6         | 4.9          |         |
| 2024 | CVPR    | [Monkey](https://github.com/Yuliang-Liu/Monkey)         | Y         | 71           | 42.6         |         |



## Citation:

If you found EST-VQA useful in your research, please kindly cite using the following BibTeX:
```
@inproceedings{wang2020general,
  title={On the general value of evidence, and bilingual scene-text visual question answering},
  author={Wang, Xinyu and Liu, Yuliang and Shen, Chunhua and Ng, Chun Chet and Luo, Canjie and Jin, Lianwen and Chan, Chee Seng and Hengel, Anton van den and Wang, Liangwei},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={10126--10135},
  year={2020}
}
```
