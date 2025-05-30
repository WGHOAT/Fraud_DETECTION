# Fraud Transaction Detection

## 📌 Objective
Build a system to classify whether a financial transaction is fraudulent or legitimate using simulated transaction data.

---

## 📊 Dataset

- **Source**: Simulated dataset of financial transactions
- **Attributes**:
  - `TRANSACTION_ID`: Unique identifier for each transaction
  - `TX_DATETIME`: Timestamp of the transaction
  - `CUSTOMER_ID`: Unique identifier for each customer
  - `TERMINAL_ID`: Identifier for the terminal/merchant
  - `TX_AMOUNT`: Transaction amount
  - `TX_TIME_SECONDS`: Seconds from start of day
  - `TX_TIME_DAYS`: Days from the beginning of the dataset
  - `TX_FRAUD`: Binary label - 0 (legitimate), 1 (fraudulent)
  - `TX_FRAUD_SCENARIO`: Indicates which fraud rule/scenario was triggered

### 🧪 Fraud Simulation Rules

1. **Rule 1**: Any transaction > 220 units is marked as fraud.
2. **Rule 2**: Two terminals chosen daily; all transactions on them over the next 28 days are fraudulent.
3. **Rule 3**: Three customers chosen daily; 1/3 of their transactions over the next 14 days are multiplied by 5 and marked as fraud.

---

## 🧹 Data Preprocessing

- Dropped non-predictive columns: `TRANSACTION_ID`, `TX_DATETIME`
- Encoded `TERMINAL_ID` with `LabelEncoder`
- Features (`X`) and label (`y`) separated
- Data split into training and test sets using an 80/20 ratio

---

## 🧠 Model

- **Algorithm**: Random Forest Classifier
- **Library**: `sklearn.ensemble`
- **Parameters**:
  - `n_estimators=100`
  - `random_state=42`

---

## 📈 Evaluation

- **Confusion Matrix**:

[[347970 0]
[ 0 2861]]
-------------------------------------------


- **Classification Report**:

| Class | Precision | Recall | F1-score | Support |
|-------|-----------|--------|----------|---------|
| 0 (Legit) | 1.00 | 1.00 | 1.00 | 347,970 |
| 1 (Fraud) | 1.00 | 1.00 | 1.00 | 2,861 |
| **Accuracy** | **1.00** |
| **Macro avg** | 1.00 | 1.00 | 1.00 |
| **Weighted avg** | 1.00 | 1.00 | 1.00 |

----------------------------------------------------------------



