"""
- Import de la bibliothêque dotenv pour lire le fichier **.env**
"""
from os import environ, path
from dotenv import load_dotenv

# Specificy a `.env` file containing key/value config values
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config:
    """Variables communes à tous les environnements"""
    FLASK_APP="app" # pour appeler le fichier app.py
    REDIS_URL=environ.get('REDIS_URL') # open source, in-memory key-value store (pour gérer la file d'attente)    


class ProdConfig(Config):
    """Variables propres à la PRODUCTION (inutile si hébergement cloud sur render.com)
    
    Dans le cadre d'un hébergement sur render.com, le fichier .env n'étant pas transmis, ces variables sont chargées manuellement sur le portail Render.
    Cette classe devient alors inutile.
    """
    FLASK_DEBUG=False # redémarre application suite à modification
    MONGODB_URI=environ.get('MONGODB_URI') # Connexion base MongoDB


class DevConfig(Config):
    """Variables propres au DEVELOPPEMENT
    
    Variable FLASK_DEBUG = True pour mise à jour automatique de l'application FLASK suite à modification de tout fichier
    
    """
    FLASK_DEBUG=True
    MONGODB_URI=environ.get('MONGODB_URI') # Connexion base MongoDB