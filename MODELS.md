# Model Documentation

This document provides detailed information about the machine learning models used for NBA game predictions.

## Over/Under (OU) Prediction Models

### XGBoost Model (Primary/Default)
**File:** `src/Train-Models/XGBoost_Model_UO.py`  
**Model Location:** `Models/XGBoost_Models/XGBoost_53.7%_UO-9.json`  
**Accuracy:** ~53.7%

**Architecture:**
- Algorithm: XGBoost Gradient Boosting
- Objective: Multi-class softmax probability (`multi:softprob`)
- Number of classes: 3 (Under, Push, Over)
- Max depth: 20
- Learning rate (eta): 0.05
- Epochs: 750

**Features:**
- Uses team statistics from both home and away teams
- Includes the over/under line as a feature
- Trained on data from 2012-24 seasons
- Multi-class classification approach (Under/Push/Over)

**Training Process:**
- Runs 100 iterations with different train/test splits (10% test size)
- Saves the best performing model based on accuracy
- Uses XGBoost's native DMatrix format for efficiency

**Prediction Output:**
- Returns probability distribution over 3 classes
- Uses argmax to determine final prediction (0=Under, 1=Push, 2=Over)

**Usage:**
```bash
python3 main.py -xgb -odds=fanduel
```

---

### Neural Network Model (Alternative)
**File:** `src/Train-Models/NN_Model_UO.py`  
**Model Location:** `Models/NN_Models/Trained-Model-OU-*`  
**Accuracy:** ~55%

**Architecture:**
- Framework: TensorFlow/Keras
- Input: Normalized team statistics + OU line
- Layers:
  - Flatten layer
  - Dense layer (128 units, ReLU6 activation)
  - Output layer (3 units, Softmax activation)

**Features:**
- Uses normalized team statistics (TensorFlow's normalize function)
- Includes the over/under line as a feature
- Trained on data from 2012-24 seasons
- Multi-class classification approach (Under/Push/Over)

**Training Process:**
- Optimizer: Adam
- Loss function: Sparse categorical crossentropy
- Epochs: 50
- Validation split: 10%
- Batch size: 32
- Callbacks: TensorBoard, Early Stopping, Model Checkpoint

**Prediction Output:**
- Returns probability distribution over 3 classes
- Uses argmax to determine final prediction (0=Under, 1=Push, 2=Over)

**Usage:**
```bash
python3 main.py -nn -odds=fanduel
```

---

### Logistic Regression Model (Experimental)
**File:** `src/Train-Models/Logistic_Regression_UO.py`  
**Status:** Training script exists but **not integrated** into prediction pipeline  
**Note:** This model is not currently used for predictions in main.py or the Flask app

**Architecture:**
- Algorithm: Logistic Regression (scikit-learn)
- Multi-class approach
- Trained on data from 2012-23 seasons

**Note:** While the training script exists, this model is not currently loaded or used in the prediction pipeline. To use it, additional integration work would be needed in the `src/Predict/` directory.

---

## Money Line (ML) Prediction Models

### XGBoost Model (Primary)
**File:** `src/Train-Models/XGBoost_Model_ML.py`  
**Model Location:** `Models/XGBoost_Models/XGBoost_68.7%_ML-4.json`  
**Accuracy:** ~68.7%

**Architecture:**
- Similar to XGBoost OU model
- Predicts home team win vs away team win
- Binary classification (2 classes)

---

### Neural Network Model (Alternative)
**File:** `src/Train-Models/NN_Model_ML.py`  
**Model Location:** `Models/NN_Models/Trained-Model-ML-*`  
**Accuracy:** ~69%

**Architecture:**
- Framework: TensorFlow/Keras
- Similar architecture to NN OU model
- Predicts home team win vs away team win
- Binary classification (2 classes)

---

## Model Selection Recommendations

### For Over/Under Predictions:
1. **Recommended: XGBoost** (`-xgb` flag)
   - Default choice for Flask web app
   - Slightly lower accuracy but more stable
   - Faster training and inference
   - Better interpretability with feature importance

2. **Alternative: Neural Network** (`-nn` flag)
   - Higher reported accuracy (~55% vs ~53.7%)
   - More complex model
   - May require more computational resources

3. **Not Recommended: Logistic Regression**
   - Training script exists but not integrated
   - Would need additional development to use

### For Money Line Predictions:
- Both XGBoost and Neural Network models perform similarly (~68-69% accuracy)
- XGBoost is the default and recommended for consistency
- Neural Network may provide slightly better accuracy

---

## Comparison: XGBoost vs Neural Network for Over/Under

| Aspect | XGBoost | Neural Network |
|--------|---------|----------------|
| Accuracy | ~53.7% | ~55% |
| Training Time | Moderate (100 iterations) | Faster (50 epochs) |
| Model Size | Larger | Smaller |
| Interpretability | High (feature importance) | Low (black box) |
| Default Usage | Yes (Flask app) | No |
| Normalization | Not required | Required |
| Framework | XGBoost | TensorFlow/Keras |

---

## Data and Features

Both models use the following features:
- Team statistics (points, rebounds, assists, etc.)
- Home and away team data
- Days of rest for both teams
- Over/under line (for OU predictions)

The dataset spans from 2012-24 seasons, as research has shown that earlier seasons (2007-2012) are less representative of current NBA gameplay.

---

## References

For more information about the methodology, see:
- `notes.txt` - Contains research papers and references
- Stanford CS229 paper referenced in notes: https://cs229.stanford.edu/proj2018/report/3.pdf
