# 📊 Analyse du churn client chez TelcoNova avec Python

## 🧩 Contexte du projet
Ce projet a pour objectif d’analyser les raisons du **churn client (attrition)** chez un opérateur fictif nommé **TelcoNova**, à partir du jeu de données public [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).

L’enjeu principal est de comprendre **pourquoi 26,6 % des clients quittent l’opérateur**, d’identifier les **profils à risque**, et de **proposer des pistes de fidélisation**.

---

## 🎯 Objectifs
- Identifier les facteurs influençant le départ des clients  
- Analyser le profil des clients churners (âge, contrat, coût mensuel, durée d’abonnement, etc.)  
- Visualiser les tendances clés à l’aide de Python  
- Formuler des recommandations stratégiques pour réduire le churn  

---

## 🛠️ Technologies utilisées
- **Python 3.10+**
- **Pandas** pour la manipulation des données  
- **NumPy** pour les calculs  
- **Matplotlib & Seaborn** pour la visualisation  
- **Jupyter Notebook** pour l’analyse exploratoire  

---

## 📁 Structure du projet
```
├── data/
│   └── telco_customer_churn.csv
├── notebooks/
│   └── analyse_churn_telco.ipynb
├── images/
│   ├── churn_distribution.png
│   ├── contrats_vs_churn.png
│   ├── tenure_vs_churn.png
│   ├── monthly_charges_vs_churn.png
│   └── recommandations.png
├── presentation/
│   └── Analyse du churn client chez TelcoNova fait par Rami NASRALLI.pptx
└── README.md
```

---

## 🔍 Principaux résultats
- **26,6 % des clients** ont quitté l’opérateur.  
- **80 % des churners** sont en contrat **mois par mois**.  
- Les **nouveaux clients (< 12 mois)** sont les plus vulnérables.  
- Les clients qui **paient plus cher** ont un risque de churn plus élevé.  

📌 **Interprétation :**  
Les clients sans engagement testent le service sans fidélité à long terme. Une tarification trop élevée ou un service perçu comme instable pousse à la résiliation.

---

## 💡 Recommandations
- Offrir des **incitatifs de fidélisation** dès les 6 premiers mois (rabais, bonus, services gratuits).  
- Créer des **formules d’engagement 6–12 mois** avec avantages clairs (support prioritaire, sécurité).  
- Mettre en place un **suivi de satisfaction précoce** (sondages automatisés, appels ciblés).  

---

## 🖼️ Présentation du projet
Une présentation PowerPoint résumant l’analyse et les recommandations est disponible :  
👉 [`Analyse du churn client chez TelcoNova fait par Rami NASRALLI.pptx`](presentation/Analyse%20du%20churn%20client%20chez%20TelcoNova%20fait%20par%20Rami%20NASRALLI.pptx)

---

## 🚀 Exécution du projet
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/Raminasralli/Analyse-du-churn-client-chez-TelcoNova-avec-Python.git
   ```
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Ouvrir le notebook :
   ```bash
   jupyter notebook notebooks/analyse_churn_telco.ipynb
   ```

---

## 👤 Auteur
**Rami NASRALLI**  
📍 Montréal, Canada  
💼 [LinkedIn](https://www.linkedin.com/in/raminasralli/)  
📧 raminasralli@gmail.com  

---

## 📚 Source du dataset
Dataset public : [Telco Customer Churn – Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---

## 🏷️ Licence
Projet à usage éducatif et analytique – libre de consultation et d’inspiration.
