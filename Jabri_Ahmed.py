# Question 1 
import yfinance as yf
# Télécharger les données de Tesla
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="1y")  # Données des 12 derniers mois
tesla_data.reset_index(inplace=True)
# Afficher les cinq premières lignes
tesla_data.head()



# Question 2 
import requests
from bs4 import BeautifulSoup
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# Exemple : extraire les données de revenus
revenues = soup.find_all("td", {"class": "number"})
tesla_revenue = [revenue.get_text() for revenue in revenues]
tesla_revenue = tesla_revenue[:5]  # Limiter à 5 résultats
tesla_revenue


# Question 3 
# Télécharger les données de GameStop
gamestop = yf.Ticker("GME")
gamestop_data = gamestop.history(period="1y")
gamestop_data.reset_index(inplace=True)
# Afficher les cinq premières lignes
gamestop_data.head()


# Question 4 
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# Extraction des données de revenus
revenues = soup.find_all("td", {"class": "number"})
gamestop_revenue = [revenue.get_text() for revenue in revenues]
gamestop_revenue = gamestop_revenue[:5]  # Limiter à 5 résultats
gamestop_revenue



#Question 5 
import matplotlib.pyplot as plt
# Visualisation pour Tesla
fig, ax1 = plt.subplots(figsize=(14, 7))
# Graphique des prix des actions
ax1.plot(tesla_data['Date'], tesla_data['Close'], color='blue', label="Prix de l'action")
ax1.set_xlabel("Date")
ax1.set_ylabel("Prix de l'action ($)", color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
# Ajouter un deuxième axe pour les revenus
ax2 = ax1.twinx()
ax2.plot(tesla_revenue, color='green', label="Revenus")
ax2.set_ylabel("Revenus ($)", color='green')
ax2.tick_params(axis='y', labelcolor='green')
# Ajouter un titre
plt.title("Tesla : Prix des Actions et Revenus")
fig.tight_layout()
plt.show()


# Question 6 
# Visualisation pour GameStop
fig, ax1 = plt.subplots(figsize=(14, 7))
# Graphique des prix des actions
ax1.plot(gamestop_data['Date'], gamestop_data['Close'], color='purple', label="Prix de l'action")
ax1.set_xlabel("Date")
ax1.set_ylabel("Prix de l'action ($)", color='purple')
ax1.tick_params(axis='y', labelcolor='purple')
# Ajouter un deuxième axe pour les revenus
ax2 = ax1.twinx()
ax2.plot(gamestop_revenue, color='orange', label="Revenus")
ax2.set_ylabel("Revenus ($)", color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
# Ajouter un titre
plt.title("GameStop : Prix des Actions et Revenus")
fig.tight_layout()
plt.show()


# Question 7
# telecharger le fichier () 