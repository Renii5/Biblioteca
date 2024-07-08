import mysql.connector
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configura la conexión a la base de datos
db_config = {
    'user': 'root',
    'password': 'Felipe021',
    'host': 'localhost',
    'database': 'biblioteca'
}

def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection


generos = ["Terror", "Accion", "Drama", "Ficcion", "Fantasia", "Historico", "Politico", "Infantil", "Suspenso"]

# Ruta principal
@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', libros=libros)

@app.route('/alta', methods=['GET', 'POST'])
def alta():
    if request.method == 'POST':
        isbn = int(request.form['isbn'])
        titulo = request.form['titulo']
        autor_nombre = request.form['autor_nombre']
        autor_apellido = request.form['autor_apellido']
        anio = request.form['anio']
        genero = request.form['genero']
        paginas = request.form['paginas']
        editorial = request.form['editorial']
        
        connection = get_db_connection()
        cursor = connection.cursor()
        
        # Verificar si el ISBN ya existe
        cursor.execute("SELECT * FROM libros WHERE isbn = %s", (isbn,))
        libro_existente = cursor.fetchone()
        
        if libro_existente:
            error = 'El ISBN ya existe. Por favor, ingrese un ISBN diferente.'
            cursor.close()
            connection.close()
            return render_template('alta.html', generos=generos, error=error)
        else:
            # Agregar el nuevo libro
            cursor.execute("INSERT INTO libros (isbn, titulo, autor_nombre, autor_apellido, anio, genero, paginas, editorial) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                           (isbn, titulo, autor_nombre, autor_apellido, anio, genero, paginas, editorial))
            connection.commit()
            cursor.close()
            connection.close()
            flash('Libro agregado exitosamente.', 'success')
            return redirect(url_for('alta'))
    
    return render_template('alta.html', generos=generos)

@app.route('/baja', methods=['GET', 'POST'])
def baja():
    if request.method == 'POST':
        isbn = int(request.form['isbn'])
        connection = get_db_connection()
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM libros WHERE isbn = %s", (isbn,))
        libro_encontrado = cursor.fetchone()
        
        if libro_encontrado:
            cursor.execute("DELETE FROM libros WHERE isbn = %s", (isbn,))
            connection.commit()
            flash('Libro eliminado exitosamente.', 'success')
        else:
            error = 'ISBN no encontrado. Por favor, intente nuevamente.'
            cursor.close()
            connection.close()
            return render_template('baja.html', error=error)
        
        cursor.close()
        connection.close()
        return redirect(url_for('baja'))
    
    return render_template('baja.html')

@app.route('/modificar', methods=['GET', 'POST'])
def modificar():
    if request.method == 'POST':
        isbn = int(request.form['isbn'])
        titulo = request.form['titulo']
        autor_nombre = request.form['autor_nombre']
        autor_apellido = request.form['autor_apellido']
        anio = request.form['anio']
        genero = request.form['genero']
        paginas = request.form['paginas']
        editorial = request.form['editorial']
        
        connection = get_db_connection()
        cursor = connection.cursor()
        
        cursor.execute("""
            UPDATE libros 
            SET titulo = %s, autor_nombre = %s, autor_apellido = %s, anio = %s, genero = %s, paginas = %s, editorial = %s 
            WHERE isbn = %s
        """, (titulo, autor_nombre, autor_apellido, anio, genero, paginas, editorial, isbn))
        connection.commit()
        
        cursor.close()
        connection.close()
        return redirect(url_for('index'))
    else:
        isbn = int(request.args.get('isbn'))
        connection = get_db_connection()
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM libros WHERE isbn = %s", (isbn,))
        libro = cursor.fetchone()
        
        cursor.close()
        connection.close()
        return render_template('modificar.html', libro=libro)

if __name__ == '__main__':
    app.run(debug=True, port=3005)


##Instale Flask,selenium, mysql