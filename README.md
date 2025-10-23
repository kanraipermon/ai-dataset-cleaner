# 🧹 AI Dataset Cleaner – Smart Preprocessing Utility

A lightweight and intelligent utility for cleaning and preprocessing machine learning datasets automatically.  
Built with Python and powered by simple AI models, this tool helps you prepare high-quality datasets for training any ML model.

---

## ✨ Features

- 🧠 **Duplicate Detection** – Find and remove identical or near-identical rows.
- 🚫 **Missing Value Handling** – Automatically fill or drop rows with missing data.
- 🧾 **Text Normalization** – Lowercasing, punctuation cleaning, emoji removal, and more.
- 📊 **Outlier Detection** – Detects and removes anomalies using AI-based algorithms.
- 📈 **Data Report Generation** – Summarizes dataset statistics and saves to CSV or HTML.

---

## ⚙️ Installation

```bash
git clone https://github.com/kanraipermon/ai-dataset-cleaner.git
cd ai-dataset-cleaner
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python cleaner.py --input your_dataset.csv --output cleaned_dataset.csv
```

**Optional arguments:**
| Argument | Description |
|-----------|--------------|
| `--drop-duplicates` | Remove duplicate rows |
| `--fill-missing mean` | Fill missing numeric values with mean |
| `--detect-outliers` | Enable AI-based outlier detection |
| `--report` | Generate data quality report |

---

## 🧩 Example

Input:
```csv
Name, Age, Salary
Alice, 25, 5000
Bob, , 6000
Alice, 25, 5000
Charlie, 120, 4000
```

Output:
```csv
Name, Age, Salary
Alice, 25, 5000
Bob, 25, 6000
Charlie, 30, 4000
```

---

## 📦 Dependencies

- pandas  
- numpy  
- scikit-learn  
- matplotlib (optional, for report visualization)

---

## ❤️ Support the Project

If you find this tool useful, consider **sponsoring** this project on GitHub to support future updates and AI-powered features.

👉 [Become a Sponsor](https://github.com/sponsors/kanraipermon)

---

## 📄 License
MIT License © 2025 [Your Name]

---

## 🧠 Future Plans

- Add language detection for multilingual datasets  
- Integration with Hugging Face Datasets  
- Web-based dashboard for interactive cleaning  
- Support for JSON, Parquet, and Excel formats  

---

**Clean data, train better AI. 🚀**
