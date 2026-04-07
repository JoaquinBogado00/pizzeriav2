# Martina - Sistema de Gestión Gastronómica 

Sistema de gestión para pizzerías desarrollado con **Python** y **Flask**, enfocado en la automatización de inventarios y optimización de la atención al cliente.

## Funcionalidades Actuales
- **Panel de Administración:** Control centralizado de pedidos y estados (Pendiente, Preparando, Entregado).
- **Gestión de Inventario (WIP):** Base de datos relacional en SQLite para el seguimiento de ingredientes.
- **Integración con WhatsApp:** Acceso directo para comunicación con clientes desde el panel.
- **Arquitectura Modular:** Separación clara de responsabilidades (Routes, Logic, Database).

## Stack Tecnológico
- **Lenguaje:** Python 3.x
- **Framework Web:** Flask
- **Base de Datos:** SQLite
- **Frontend:** HTML5, CSS3 (JinJa2 Templates)

## En Desarrollo (Roadmap)
- [ ] Implementación de lógica de descuento automático de stock basada en recetas.
- [ ] Sistema de alertas de cantidad mínima para reabastecimiento.
- [ ] Reportes de ventas diarios.

## Instalación
1. Clonar el repositorio.
2. Crear un entorno virtual: `python -m venv venv`.
3. Instalar dependencias: `pip install -r requirements.txt`.
4. Ejecutar: `python app.py`.