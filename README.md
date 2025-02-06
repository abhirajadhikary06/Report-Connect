# 🚨 AI-Powered Crime Hotspot Prediction & Reporting Platform

## 📌 **Overview**
This project is an **AI-driven platform** that allows users to **anonymously report harassment cases** while utilizing **Machine Learning** to predict potential **crime hotspots**. By combining **crowdsourced data** and **AI-based analysis**, it helps authorities and the public identify **high-risk areas** and take preventive measures.

## 🔥 **Key Features**

### ✅ **1. Anonymous & Secure Reporting**
- Users can **report harassment cases** without revealing their identity.
- The reports include **location, type of harassment, and description**.

### 🌍 **2. Real-Time Crime Mapping**
- A **dynamic map** displays reported harassment cases as **red blurry markers**.
- **More reports = Higher intensity**, helping visualize crime-prone areas.

### 🤖 **3. AI-Powered Hotspot Prediction**
- Uses **Kernel Density Estimation (KDE)** to predict the **next potential crime hotspot**.
- The predicted hotspot is **marked in green**, with intensity decreasing from the most severe to least severe.

### 📈 **4. Data-Driven Insights**
- A **curved graph** dynamically updates to show crime trends across different locations.
- The system **highlights the area with the most reports in real-time**.

### 🔍 **5. Crowdsourced Data Collection**
- Community-driven **data collection** improves predictive accuracy.
- Allows **law enforcement and citizens** to stay informed about crime patterns.

### ⚡ **6. Scalability & Future Expansion**
- Designed to handle **large-scale data entries**.
- Initially, a **CSV dataset with 10,000 reports** will populate the database for AI model training.
- After reaching this milestone, reports will be **manually submitted** by users.

---

## 🛠 **Tech Stack**

### **Backend** 🖥️
- **Django (Python)** for server-side processing.
- **SQLite3** for managing reports and predictions.

### **Frontend** 🐥
- **HTML, JavaScript, Bulma CSS** for an intuitive user experience.
- **Leaflet.js & OpenStreetMap API** for map visualization.

### **Machine Learning & AI** 🤖
- **Kernel Density Estimation (KDE)** for hotspot prediction.
- **Pandas & NumPy** for data processing.

---

## 🔄 **How It Works**

### 1️⃣ **Report Submission**
- Users enter **location, type of harassment, and description**.
- The system **automatically fetches latitude & longitude** based on the location name.
- The report is stored securely in the **database**.

### 2️⃣ **Real-Time Visualization**
- A **map dynamically updates** to reflect new reports.
- **Crime hotspots are predicted using AI**, ensuring proactive safety measures.

### 3️⃣ **Prediction Mechanism**
- The AI model **analyzes historical crime data**.
- KDE determines the **most likely future crime locations**.
- The **top 5 hotspots are displayed with decreasing intensity** (green border with blurred green inside).

---

## 📂 **Setting Up the Project**

### 🔧 **1. Clone the Repository**
```bash
    git clone https://github.com/yourusername/Report-Connect.git
    cd Report-Connect
```

### 📦 **2. Install Dependencies**
```bash
    pip install -r requirements.txt
```

### 🔥 **3. Run Migrations & Start Server**
```bash
    python manage.py migrate
    python manage.py runserver
```

---

## 🚀 **Future Enhancements**
- **Advanced AI Models**: Improve prediction accuracy with **Deep Learning**.
- **User Alerts**: Send notifications when users are in **high-risk zones**.
- **Integration with Law Enforcement**: Provide verified data to **help authorities take action**.
- **Multilingual Support**: Expand accessibility to a **wider audience**.

---

## 🏆 **Impact & Goals**
- **Empower communities** to report incidents without fear.
- **Assist law enforcement** in focusing efforts on high-risk areas.
- **Utilize AI & Big Data** for **proactive crime prevention**.

🫂 *Together, we can make cities safer!* 🔥

