from website import create_app

app = create_app()

if __name__ == '__main__':
    
    app.config['AVATARS_SAVE_PATH'] = "./static/images"
    app.run(debug=True)
