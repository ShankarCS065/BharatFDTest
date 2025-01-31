# 📝 Django FAQ API

A **Django REST API** for managing FAQs with **multilingual support**, **Redis caching**, and **Docker deployment**.

## **🚀 Features**
- ✅ **Django REST API** for managing FAQs
- ✅ **Multilingual support** (Google Translate API)
- ✅ **Rich-text editor (CKEditor 5)**
- ✅ **Redis caching for faster performance**
- ✅ **Docker support for easy deployment**
- ✅ **Django Admin Panel for FAQ management**

---

# **📌 1️⃣ Installation Guide (Windows)**

### **🔹 Step 1: Clone the Repository**
```bash
git clone https://github.com/yourusername/django-faq-api.git
cd django-faq-api
```
### **🔹 Step 2: Set Up a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Activate the virtual environment
```
### **🔹 Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
### **🔹 Step 4: Set Up Environment Variables
Create a .env file in the project root:
```makefile
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
```
### **🔹 Step 5: Apply Database Migrations
```bash
python manage.py migrate
```
### **🔹 Step 6: Create a Superuser
As your need...
```bash
python manage.py createsuperuser  
```
Follow the prompts to set a username, email, and password.
### **🔹 Step 7: Start Redis Server
If Redis is not running, start it manually:
```bash
redis-server
```
Then test Redis is running:
```bash
redis-cli ping
```
Expected output:
```bash
PONG
```
### **🔹 Step 8: Start Django Server
```bash
python manage.py runserver
```
Your API will be available at http://127.0.0.1:8000/api/.

# **📌 2️⃣ Running with Docker**
### **🔹 Step 1: Install Docker
 Download and install "Docker Desktop".
 
### **🔹 Step 2: Build and Run Containers
```bash
docker-compose build --no-cache
docker-compose up -d
```
This will start Django + Redis inside Docker.

### **🔹 Step 3: Verify Running Containers
```bash
docker ps
```
You should see both django_app and redis_cache running.

# **📌 3️⃣ API Usage Examples**
### **🔹 Fetch All FAQs (English)
```bash
curl http://127.0.0.1:8000/api/faqs/
```
### **🔹 Fetch FAQs in Hindi
```bash
curl http://127.0.0.1:8000/api/faqs/?lang=hi
```
### **🔹 Fetch FAQs in Bengali
```bash
curl http://127.0.0.1:8000/api/faqs/?lang=bn
```

# **📌 4️⃣ Django Admin Panel**
To access the Django Admin Panel, go to: 🔗 http://127.0.0.1:8000/admin/
Log in using the superuser credentials created in Step 6.

# **📌 5️⃣ Contribution Guidelines**
### **🔹 How to Contribute
1.Fork the repository on GitHub.
2.Clone your forked repo:
```bash
git clone https://github.com/yourusername/django-faq-api.git
cd django-faq-api
```
3.Create a new branch:
```bash
git checkout -b feature-new-api-endpoint
```
4.Make changes and commit:
```bash
git add .
git commit -m "feat: Add new API endpoint for FAQs"
```
5.Push changes to GitHub:
```bash
git push origin feature-new-api-endpoint
```
6.Open a Pull Request on GitHub.

# **📌 6️⃣ Troubleshooting**
❌ Error: "redis-server not found"
✔ Solution: Install Redis for Windows and start it manually:
```bash
redis-server
```
❌ Error: "Django 5.1.5 requires Python ≥3.10"
✔ Solution: Update your Dockerfile to use Python 3.11.

❌ Error: "Page not found (404) on /"
✔ Solution: Ensure faq_project/urls.py has:

```python
from django.http import HttpResponseRedirect
urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/api/')),  # Redirect `/` to `/api/`
    path('admin/', admin.site.urls),
    path('api/', include('faqs.urls')),
]

```










