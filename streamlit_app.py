import streamlit as st

st.set_page_config(
    page_title='Article Automatisation Python by Naltos',
    page_icon='🤖'
)

st.title("Automatisation windows 🪐")
st.write("Tu en as marre de répéter certaines action et tu souhaites les automatiser ? Regarde donc ce tuto !")

tab1, tab2, tab3, tab4 = st.tabs(["Introduction", "Installation", "Code", "Exercice"])

with tab1:
    st.header("Qu'allons nous faire ?")
    st.write("Dans ce tuto, nous allons apprendre à **:blue[automatiser]** la :green[création] / :green[modification] / :green[lecture et suppresion] de nos fichiers ainsi que de nos dossiers !")
    st.header("Quels sont les prérequis pour suivre ce tuto ?")
    st.write("- Connaître les bases de la programmation en Python (ex: Fonctions, Modules, Conditions, etc)")
    st.write("- D'un IDE quelconque (ex: VSCode, Notepad++, Spyder)")
    st.write("- ~~D'un virement de 200e à Naltos~~")
    st.header("C'est parti !⚡️")
    
with tab2:
    st.header("📦 Les modules nécessaires à ce tuto :")    
    st.write("- OS")
    st.write("- Rich")
    code = '''pip install Rich'''
    st.code(code, language='python')
    st.write("- Pathlib")
    st.write("Les autres modules nécessaires à ce tuto sont intégrés de base à Python, nous n'avons donc pas besoin de les installer.")
    
    st.header("🔎 A quoi vont-ils servirent ?")
    st.write("- OS va nous permettre d'intéragir avec notre système d'exploitation")
    st.write("- Rich servira seulement à styliser notre console")
    st.write('- Pathlib va nous permettre de parcourir nos différents dossiers')
    
with tab3:
    st.header("💻 A vos marque, prêt, codez !")
    st.write("Attaquons nous à la base de notre code, nous allons définir une fonction 'main' qui nous servira d'executable pour le reste de nos fonctions:")
    code = ('''
            def main():
                pass
                
            if __name__ == "__main__":
                main()
            ''')
    st.code(code, language='python')
    st.write("Pour l'instant, nous n'avons aucune fonctions à exécuter donc nous utilisons le mot clé 'pass' pour indiquer à notre code d'ignorer cette fonction.")
    st.write("La seconde ligne est une condition qui permet de vérifier que le fichier exécuter est bien le fichier racine de notre projet.")
    
    st.header("Ecrivons notre première fonction !")
    st.write("Pour cette première fonction, nous allons automatiser la création d'un dossier:")
    create_mkdir = ('''
                    # Ici, on indique le type de nos arguments (donc ici string) ainsi que le type de retour de notre fonction (également string)
                    def create_mkdir(path: str, directory_name: str) -> str:
                        # not isinstance permet de vérifier si la valeur passer dans notre variable path est bien de type string
                        if not isinstance(path, str):
                            print("Valeur incorrect!")
                        # Pareil pour ici
                        elif not isinstance(directory_name, str):
                            print("Valeur incorrect!")
                        else:
                            os.mkdir(path + directory_name)
                            console.print("Dossier créer avec succès ! => [cyan]{}{}[/]".format(path, directory_name), style='bold underline green')
                    ''')
    st.code(create_mkdir, language='python')
    st.write("Pour exécuter cette fonction, nous avons besoin de la rajouter dans notre fonction main():")
    main = ('''
            def main():
                create_mkdir()
                
            if __name__ == "__main__":
                main()
    ''')
    st.code(main, language='python')
    st.write("Seulement, nous avons spécifiés des arguments à passer dans notre fonction plus haut, nous avons donc besoin de les récupérer:")
    main2 = ('''
            def main():
                path = console.input("[bold blue]Merci de spécifier le chemin d'accès dans lequel vous souhaitez créer votre dossier: [/]")
                directory_name = console.input("[bold blue]Merci de spécifier le nom du dossier que vous souhaitez créer [bold underline red](Merci de ne pas mettre d'espace, seulement des caractères spéciaux: '_, -')[/]: [bold magenta]")
                create_mkdir(path, directory_name)
                
            if __name__ == "__main__":
                main()
    ''')
    st.code(main2, language='python')
    st.write("Et voilà, vous venez de créer avec succès votre premier dossier depuis une ligne de commande !")
    
with tab4:
    st.header("📓 Exercice")
    st.write("Afin de tester vos nouvelles connaissances, voici une série de fonctions que vous pouvez coder:")
    st.write('- Une fonction qui permet de supprimer un dossier.')
    st.write('- Une fonction qui permet de lister les éléments d\'un dossier.')
    st.write('- Permettre à l\'utilisateur de choisir quel action il souhaite exécuter.')
    st.header("🧠 Bon chance !")
    st.image(
        "https://media.giphy.com/media/rHR8qP1mC5V3G/giphy.gif",
        width=400
    )
