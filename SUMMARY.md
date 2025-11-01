# Summary: Over/Under Modeling Methods Identification

## Question
**"Identify what method is being used for the over/under modelling and predictions, is it all xgboost or is it through linear regression?"**

## Answer

### Primary Method: **XGBoost** (Default)
The primary and default method for over/under (OU) predictions is **XGBoost**, not linear regression.

**Evidence:**
- The main.py default command uses `-xgb` flag
- The Flask web app (used for browser-based predictions) exclusively uses XGBoost
- The README documentation recommends XGBoost
- Model file: `Models/XGBoost_Models/XGBoost_53.7%_UO-9.json`
- Accuracy: ~53.7%

### Alternative Method: **Neural Network**
An alternative method using TensorFlow/Keras Neural Networks is also available.

**Evidence:**
- Can be invoked with `-nn` flag
- Model file: `Models/NN_Models/Trained-Model-OU-1699315414.2268295`
- Accuracy: ~55%

### Experimental: **Logistic Regression** (Not Used)
While a Logistic Regression training script exists, it is **NOT integrated** into the prediction pipeline.

**Evidence:**
- Training file exists: `src/Train-Models/Logistic_Regression_UO.py`
- No corresponding prediction runner in `src/Predict/`
- Not used by main.py or Flask app
- Would require additional development to use

## Summary Table

| Method | Status | Accuracy | Used By | File Location |
|--------|--------|----------|---------|---------------|
| **XGBoost** | ✅ Primary/Default | ~53.7% | main.py, Flask app | `XGBoost_Runner.py` |
| **Neural Network** | ✅ Alternative | ~55% | main.py (with -nn flag) | `NN_Runner.py` |
| **Logistic Regression** | ❌ Not Integrated | Unknown | None | Training only |

## Conclusion

**The over/under predictions use XGBoost by default, NOT linear regression.** 

While Logistic Regression training code exists in the repository, it is not currently integrated into the prediction pipeline and is not used for any actual predictions. Users can also choose to use Neural Networks as an alternative to XGBoost.

## Documentation Updates

To clarify this, the following documentation has been added/updated:

1. **README.md** - Added "Prediction Models" section clearly identifying XGBoost as primary
2. **MODELS.md** - New comprehensive technical documentation about all models
3. **Inline Code Comments** - Added module-level documentation to all prediction and training files
4. **Usage Examples** - Updated to show different model selection options

These changes ensure future users can easily understand which methods are available and which are actually used for predictions.
