# RandomPassword

Application Python avec interface tkinter pour generer instantanement 10 mots de passe forts, avec copie en un clic et retour visuel immediat.

Chaque mot de passe suit une composition fixe:
- generation de 10 mots de passe a la demande,
- chaque mot de passe contient exactement:
  - 2 lettres majuscules,
  - 3 chiffres,
  - 2 caracteres speciaux,
  - 13 lettres minuscules,
- bouton Copier pour chaque mot de passe,
- feedback visuel (texte en rouge pendant 1 seconde apres copie).

## Structure

- `password_generator_app.py`: application complete (interface + generation)
- `docs/documentation.html`: documentation HTML ouvrable depuis l'application
- `docs/changelog.html`: changelog HTML ouvrable depuis l'application

## Lancer l'application

Depuis le dossier du projet:

```bash
python3 password_generator_app.py
```

Sous Windows, vous pouvez aussi lancer directement:

```bat
lancer_app_windows.bat
```
