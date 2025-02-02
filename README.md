# 📖 FAQ Management System

This is a **Django-based FAQ management system** that supports **multilingual content** and caching using **Redis**. It provides a **REST API** for managing FAQs and supports translations in **English, Hindi, and Bengali**.

---

## 🚀 Features

✅ **Multilingual Support** – Automatically translates FAQs into Hindi and Bengali.  
✅ **WYSIWYG Editor** – Uses **CKEditor** for rich text formatting.  
✅ **Caching** – Speeds up responses using **Redis**.  
✅ **REST API** – Provides endpoints for managing FAQs efficiently.

---

## 🛠 Installation

### **Prerequisites**
- Python **3.8** or higher
- Redis server
- Docker (**optional**, for deployment)

### **Setup Instructions**

1️⃣ **Clone the repository:**  
```bash
 git clone https://github.com/yourusername/faq_project.git
 cd faq_project
```

2️⃣ **Create and activate a virtual environment:**  
```bash
python -m venv env
# Activate the virtual environment
# On Windows:
.env\Scripts\activate
# On Mac/Linux:
source env/bin/activate
```

3️⃣ **Install dependencies:**  
```bash
pip install -r requirements.txt
```

4️⃣ **Run migrations:**  
```bash
python manage.py migrate
```

5️⃣ **Start the development server:**  
```bash
python manage.py runserver
```

6️⃣ **Access the API:**  
Navigate to: [http://127.0.0.1:8000/api/faqs/](http://127.0.0.1:8000/api/faqs/)

---

## 🔥 API Usage

### 📌 **Endpoints**
| Method | Endpoint | Description |
|--------|----------------------|----------------------|
| **GET** | `/api/faqs/` | Fetch all FAQs (default: English) |
| **GET** | `/api/faqs/?lang=hi` | Fetch FAQs in Hindi |
| **GET** | `/api/faqs/?lang=bn` | Fetch FAQs in Bengali |

### 📝 **Example Requests**

📌 **Using cURL:**  
```bash
curl http://127.0.0.1:8000/api/faqs/
```

📌 **Using Python requests:**  
```python
import requests
response = requests.get("http://127.0.0.1:8000/api/faqs/")
print(response.json())
```

---

## 📜 License
This project is licensed under the **MIT License**.

👨‍💻 Developed by [MD Faizan Ahmed](https://github.com/faizanjarjez)

