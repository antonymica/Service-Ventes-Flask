
# Projet Backend Flask avec Docker

Ce projet utilise Flask comme framework backend et Docker pour la conteneurisation. Vous trouverez ici les instructions pour démarrer l'application à l'aide des fichiers `Dockerfile` et `docker-compose.yml`.

## Prérequis

Avant de commencer, assurez-vous que les outils suivants sont installés sur votre machine :

- [Docker](https://www.docker.com/get-started) (version 20.10 ou supérieure)
- [Docker Compose](https://docs.docker.com/compose/) (version 1.29 ou supérieure)

## Installation

1. **Clonez le repository :**

    Clonez le projet sur votre machine locale :

    ```bash
    git clone https://github.com/antonymica/Service-Ventes-Flask.git
    cd Service-Ventes-Flask
    ```

2. **Démarrez le projet avec Docker Compose :**
    
    Utilisez docker-compose.yml pour démarrer l'application avec tous les services nécessaires :
    
    ```bash
    docker-compose up --build -d
    ```
    Cela va :

        - Construire l'image du backend Flask à l'aide du Dockerfile.
        
        - Démarrer le conteneur Flask et tous les autres services définis dans le docker-compose.yml.

3. **Accéder à l'application:**
    
    Une fois que les conteneurs sont démarrés, vous pouvez accéder à l'application Flask en ouvrant un navigateur et en allant sur l'URL suivante :
    
    ```bash
    http://localhost:5000/ventes/
    ```
    Vous pouvez faire tous les requests: GET, POST, PUT, DELETE

# License :

### Explication :
- **Installation** : Instructions pour cloner et installer le projet.
- **Docker** : Explication sur l'utilisation de Docker pour construire et lancer le projet.
- **Commandes Docker** : Pour la gestion des conteneurs (voir, arrêter, redémarrer).
- **Développement et Debugging** : Explication de la configuration pour le développement et la gestion des erreurs.
