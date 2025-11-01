# NBA Sports Betting Using Machine Learning 🏀
<img src="https://github.com/kyleskom/NBA-Machine-Learning-Sports-Betting/blob/master/Screenshots/output.png" width="1010" height="292" />

A machine learning AI used to predict the winners and under/overs of NBA games. Takes all team data from the 2007-08 season to current season, matched with odds of those games, using machine learning models to predict winning bets for today's games. Achieves ~69% accuracy on money lines and ~55% on under/overs. Outputs expected value for teams money lines to provide better insight. The fraction of your bankroll to bet based on the Kelly Criterion is also outputted. Note that a popular, less risky approach is to bet 50% of the stake recommended by the Kelly Criterion.

## Prediction Models

This project supports multiple machine learning models for predictions:

### Money Line Predictions
- **XGBoost** (Primary) - Achieves ~68.7% accuracy
- **Neural Network** (Alternative) - Achieves ~69% accuracy

### Over/Under Predictions
- **XGBoost** (Primary/Default) - Achieves ~53.7% accuracy
  - Used by default when running `-xgb` flag
  - Uses gradient boosting with multi-class classification (Under/Push/Over)
  - Model file: `Models/XGBoost_Models/XGBoost_53.7%_UO-9.json`
- **Neural Network** (Alternative) - Achieves ~55% accuracy
  - Can be used with `-nn` flag
  - Uses TensorFlow/Keras with fully connected layers
  - Model file: `Models/NN_Models/Trained-Model-OU-*`

**Note:** While a Logistic Regression training script exists (`src/Train-Models/Logistic_Regression_UO.py`), it is not currently integrated into the prediction pipeline. The primary method for over/under predictions is **XGBoost**, which is used by the Flask web app and recommended for general use.

📖 **For detailed technical information about the models, architectures, and training processes, see [MODELS.md](MODELS.md)**
## Packages Used

Use Python 3.11. In particular the packages/libraries used are...

* Tensorflow - Machine learning library
* XGBoost - Gradient boosting framework
* Numpy - Package for scientific computing in Python
* Pandas - Data manipulation and analysis
* Colorama - Color text output
* Tqdm - Progress bars
* Requests - Http library
* Scikit_learn - Machine learning library

## Usage

<img src="https://github.com/kyleskom/NBA-Machine-Learning-Sports-Betting/blob/master/Screenshots/Expected_value.png" width="1010" height="424" />

Make sure all packages above are installed.

```bash
$ git clone https://github.com/kyleskom/NBA-Machine-Learning-Sports-Betting.git
$ cd NBA-Machine-Learning-Sports-Betting
$ pip3 install -r requirements.txt
$ python3 main.py -xgb -odds=fanduel
```

### Command Line Options

**Model Selection:**
- `-xgb` - Use XGBoost models for predictions (recommended, default for over/under)
- `-nn` - Use Neural Network models for predictions
- `-A` - Run all models and compare predictions

**Odds Options:**
Odds data will be automatically fetched from sbrodds if the -odds option is provided with a sportsbook.  Options include: fanduel, draftkings, betmgm, pointsbet, caesars, wynn, bet_rivers_ny

If `-odds` is not given, enter the under/over and odds for today's games manually after starting the script.

**Additional Options:**
- `-kc` - Calculate and display the recommended fraction of your bankroll to wager based on the model's edge (Kelly Criterion)

**Examples:**
```bash
# Use XGBoost model with FanDuel odds
$ python3 main.py -xgb -odds=fanduel

# Use Neural Network model with DraftKings odds  
$ python3 main.py -nn -odds=draftkings

# Compare all models with Kelly Criterion
$ python3 main.py -A -odds=betmgm -kc
```

## Flask Web App
<img src="https://github.com/kyleskom/NBA-Machine-Learning-Sports-Betting/blob/master/Screenshots/Flask-App.png" width="922" height="580" />

This repo also includes a small Flask application to help view the data from this tool in the browser.  To run it:
```
cd Flask
flask --debug run
```

## Getting new data and training models
```
# Create dataset with the latest data for 2023-24 season
cd src/Process-Data
python -m Get_Data
python -m Get_Odds_Data
python -m Create_Games

# Train XGBoost models (primary/recommended)
cd ../Train-Models
python -m XGBoost_Model_ML    # Money line model
python -m XGBoost_Model_UO    # Over/Under model

# Train Neural Network models (alternative)
python -m NN_Model_ML         # Money line model
python -m NN_Model_UO         # Over/Under model

# Train Logistic Regression (experimental, not used in predictions)
python -m Logistic_Regression_ML
python -m Logistic_Regression_UO
```

## Contributing

All contributions welcomed and encouraged.
