# 🏛️ The Scholastic Registry & Analytics Suite

**Status:** *Deployed & Operational* **Architecture:** *Enterprise-Grade Modular MVC*

---

### 🧐 Overview

Welcome to **The Scholastic Registry**, a refined data management solution designed to streamline the student enrollment process. This application serves as a comprehensive bridge between raw data entry and high-level administrative oversight. 

Constructed with the **Streamlit** framework and fortified by a **SQLite** backend, this suite demonstrates a professional commitment to the *Separation of Concerns* principle, ensuring that data logic, user interface, and controller mechanisms operate in harmonious isolation.

### ✨ Key Features

* **🎓 Student Registration Interface:** A user-centric form designed for the seamless capture of candidate demographics, including age verification, geographic origin, and academic subject selection.
* **🛡️ Secure Administrative Command Center:** A password-protected environment granting authorized personnel full sovereignty over the dataset.
* **📊 Bespoke Analytics Dashboard:** Integrated **Plotly** visualizations that transform raw enrollment data into actionable insights, featuring gender distribution ratios and geographic enrollment metrics.
* **⚠️ Safe-Guard Deletion Protocols:** An elegant modal interface that prevents accidental data loss, requiring explicit confirmation before purging records from the persistent storage.

### 🏗️ Technical Architecture

This repository eschews the monolithic approach in favor of a scalable, enterprise-ready file structure:

* **`database.py` (The Model):** Handles all SQLite transactions and schema definitions with absolute precision.
* **`views/` (The View):** Distinct modules for `student_form` and `admin_dashboard` ensuring the UI remains crisp and unburdened by logic.
* **`app.py` (The Controller):** The central orchestrator that routes user traffic to the appropriate interface.

### 🛠️ Technology Stack

* **Frontend Framework:** Streamlit
* **Data Persistence:** SQLite3
* **Data Manipulation:** Pandas
* **Visual Analytics:** Plotly Express

### 🚀 Getting Started

To inaugurate this suite on your local machine, kindly follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/scholastic-registry.git](https://github.com/your-username/scholastic-registry.git)
    ```

2.  **Install Dependencies:**
    Ensure your environment is prepared by installing the requisite packages.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch the Application:**
    Initiate the server to begin the session.
    ```bash
    streamlit run app.py
    ```

---
*Crafted with Python and a touch of elegance.*