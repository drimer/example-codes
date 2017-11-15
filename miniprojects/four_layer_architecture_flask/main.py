from dependency_injection.container import DIContainer

if __name__ == '__main__':
    app = DIContainer().app
    app.run()
