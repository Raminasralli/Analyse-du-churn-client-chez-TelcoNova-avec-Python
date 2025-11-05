# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Nettoyage
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df_cleaned = df.dropna(subset=['TotalCharges'])

# Calcul du coût moyen par groupe churn
mean_costs = df.groupby('Churn')['MonthlyCharges'].mean()
print("Coût mensuel moyen :")
print(f"Clients churners : {mean_costs['Yes']:.2f} $")
print(f"Clients fidèles  : {mean_costs['No']:.2f} $")

# Nombre de churners par type de contrat
churn_counts = df[df['Churn'] == 'Yes'].groupby('Contract').size()

# Nombre total de clients par type de contrat
total_counts = df.groupby('Contract').size()

# Taux de churn par type de contrat (optionnel)
churn_rate = (churn_counts / total_counts * 100).round(2)

# Affichage
print("Nombre de churners par type de contrat :")
print(churn_counts)
print("\nNombre total de clients par type de contrat :")
print(total_counts)
print("\nTaux de churn par type de contrat (%):")
print(churn_rate)

# Configuration des visualisations
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Graphique 1 : Répartition globale du churn
sns.countplot(data=df_cleaned, x='Churn', palette='pastel')
plt.title("Répartition du churn chez les clients")
plt.xlabel("Client a quitté l'opérateur ?")
plt.ylabel("Nombre de clients")
plt.show()

# Graphique 2 : Churn par type de contrat
sns.countplot(data=df_cleaned, x='Contract', hue='Churn', palette='Set2')
plt.title("Churn par type de contrat")
plt.xlabel("Type de contrat")
plt.ylabel("Nombre de clients")
plt.legend(title="Churn")
plt.show()

# Graphique 3 : Churn par ancienneté
sns.histplot(data=df_cleaned, x='tenure', hue='Churn', bins=30, multiple='stack', palette='coolwarm')
plt.title("Répartition du churn selon l'ancienneté")
plt.xlabel("Ancienneté (en mois)")
plt.ylabel("Nombre de clients")
plt.show()

# Graphique 4 : Coût mensuel selon churn
sns.boxplot(data=df_cleaned, x='Churn', y='MonthlyCharges', palette='Set3')
plt.title("Coût mensuel selon churn")
plt.xlabel("Client a quitté l'opérateur ?")
plt.ylabel("Montant mensuel ($)")
plt.show()

# Graphique 5 : Corrélations entre variables numériques
corr = df_cleaned[['tenure', 'MonthlyCharges', 'TotalCharges']].corr()
sns.heatmap(corr, annot=True, cmap='Blues', fmt=".2f", square=True)
plt.title("Corrélation entre variables numériques")
plt.show()
