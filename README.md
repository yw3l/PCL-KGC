## How to Run

It involves 3 steps: dataset preprocessing, model training, and model evaluation.

For WN18RR and FB15k237 datasets, we use files from [KG-BERT](https://github.com/yao8839836/kg-bert).

### WN18RR dataset

Step 1, preprocess the dataset
```
bash scripts/preprocess.sh WN18RR
```

Step 2, training the model and (optionally) specify the output directory (< 3 hours)
```
OUTPUT_DIR=./checkpoint/wn18rr/ bash scripts/train_wn.sh
```

Step 3, evaluate a trained model
```
bash scripts/eval.sh ./checkpoint/wn18rr/model_last.mdl WN18RR
```

Feel free to change the output directory to any path you think appropriate.

### FB15k-237 dataset

Step 1, preprocess the dataset
```
bash scripts/preprocess.sh FB15k237
```

Step 2, training the model and (optionally) specify the output directory (< 3 hours)
```
OUTPUT_DIR=./checkpoint/fb15k237/ bash scripts/train_fb.sh
```

Step 3, evaluate a trained model
```
bash scripts/eval.sh ./checkpoint/fb15k237/model_last.mdl FB15k237
```
