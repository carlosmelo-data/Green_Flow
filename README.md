# Green_Flow
Repositório para o projeto Green Flow, do curso de DataOps.

# 📊 Startup Data Challenge -- Insights Sustentáveis com Parquet

## 📖 Overview  
This project automates **sensors data collection**, processes it, and displays an **interactive dashboard** using **gradio**.  
It gathers **environmental sustainability data** using parquet files.  

The collected data is processed **pandas** and presented in **gradio**.  

---

## 🛠️ Tech Stack  
- **Python 3.12+**  
- **Gradio** (Machine Learning demonstration app)  
- **Docker** (Containerized execution)  

---

## 🔧 Installation & Setup  

### 1️ Clone the Repository  
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo

### 2 Build the docker image
```sh
docker build -t greenflow .

### 3 Run the application
```sh
docker run -p 7878:7878 greenflow:latest

