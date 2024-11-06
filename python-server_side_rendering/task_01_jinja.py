#!/usr/bin/python3
"""Flask application for Techium website."""
import typer
from flask import Flask, render_template
import asyncio
import importlib.util
import sys

async def check_and_install_typer():
    # Vérifier si Typer est installé
    if importlib.util.find_spec('typer') is None:
        print("Typer n'est pas installé. Installation en cours...")
        
        # Créer et exécuter le processus d'installation
        process = await asyncio.create_subprocess_exec(
            sys.executable, '-m', 'pip', 'install', 'typer',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        # Attendre que l'installation soit terminée
        stdout, stderr = await process.communicate()
        
        if process.returncode == 0:
            print("Typer a été installé avec succès!")
            return True
        else:
            print(f"Erreur lors de l'installation: {stderr.decode()}")
            return False
    return True


app = Flask(__name__)
cli = typer.Typer()

@app.route('/')
def home():
    """Home page route."""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page route."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Contact page route."""
    return render_template('contact.html')

@cli.command()
def run(port: int = 5000, debug: bool = True):
    """Run the Flask application with Typer CLI."""
    typer.secho(f"✨ Starting Techium on port {port}", fg=typer.colors.GREEN)
    app.run(debug=debug, port=port)

if __name__ == "__main__":
    asyncio.run(check_and_install_typer())
    cli()