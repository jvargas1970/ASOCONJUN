<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Validar carnet colegiado</title>
</head>
<body>
    <h1>Validar carnet colegiado</h1>
    <form method="post" action="{% url 'validar_carnet' %}">
        {% csrf_token %}
        <label for="carnet_colegiado">Carnet colegiado:</label><br>
        <input type="text" name="carnet_colegiado" id="carnet_colegiado" required><br><br>
        <button type="submit">Validar</button>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>