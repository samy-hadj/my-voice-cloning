# Projet de Clonage de Voix avec Bark et HuBERT

## Description du Projet

Le clonage de voix est une technologie qui permet de créer des répliques numériques d'une voix humaine, en reproduisant fidèlement des caractéristiques telles que le timbre, l'intonation, et le style de parole. Ce projet exploite des modèles avancés comme **Bark** pour la synthèse vocale et **HuBERT** pour l'analyse des caractéristiques audio.

Grâce à des techniques d'apprentissage profond, le clonage de voix permet de générer un discours imitant un locuteur spécifique à partir d'un échantillon vocal limité. Le projet peut être utilisé dans divers domaines, tels que :
- La génération de doublages pour des médias
- La création de voix pour des assistants virtuels
- La personnalisation du contenu audio

Cependant, ce type de technologie pose des questions éthiques, notamment en termes de confidentialité et d'authenticité des données vocales.

## Créateurs

Ce projet a été réalisé par **Samy Hadj-Said**, **Jason Perez**, et **Briac Six**.

## Démonstration

Vous pouvez consulter la démonstration complète sur Google Colab en suivant [ce lien](https://colab.research.google.com/drive/1kRR49HINV5_EeorFLMiMd9AeQm--gfmX?usp=sharing).

## Installation

Pour exécuter ce projet, vous aurez besoin d'installer les bibliothèques suivantes :
- bark-voice-cloning-HuBERT-quantizer
- bark

## Utilisation

1. **Chargement des modèles Bark et HuBERT** : Charger les modèles nécessaires pour la génération et la manipulation de l'audio.
2. **Génération d'Audio à Partir de Texte** : Générer un fichier audio à partir d'un texte fourni en entrée.
3. **Préparation de l'audio à cloner et des modèles** : Configurer les modèles et préparer l'audio pour le clonage.
4. **Extraction des Tokens Sémantiques avec HuBERT** : Extraire les tokens sémantiques de l'audio avec le modèle HuBERT.
5. **Génération d'Audio avec la Voix Clonée** : Utiliser les tokens extraits pour générer un fichier audio avec la voix clonée.

## Fichiers Importants

- `bark-voice-cloning-HuBERT-quantizer`: Modèle pour l'extraction de tokens sémantiques avec HuBERT.
- `bark`: Modèle pour la synthèse vocale.
- `audio.wav`: Exemple d'audio à cloner.
- `output.npz`: Fichier contenant les prompts générés pour la génération d'audio.

## Références et Documentation

- [Bark GitHub Repository](https://github.com/serp-ai/bark-with-voice-clone)
- [HuBERT GitHub Repository](https://github.com/gitmylo/bark-voice-cloning-HuBERT-quantizer)
- [Coqui TTS](https://github.com/coqui-ai/TTS)

## Enjeux Éthiques

Bien que la technologie de clonage de voix soit fascinante et ouvre de nombreuses perspectives, elle pose des questions éthiques, notamment concernant l'authenticité des voix et la protection des données personnelles. Il est essentiel d’utiliser ces technologies de manière responsable.

## License

Ce projet est sous la licence [MIT](https://opensource.org/licenses/MIT).
