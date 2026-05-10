#!/bin/bash

echo "🚀 Iniciando despliegue de agentes locales..."

# 1, 2 y 3: Revisar, borrar y recrear la carpeta .custom_agents
if [ -d ".custom_agents" ]; then
    echo "🗑️ Borrando carpeta .custom_agents existente..."
    rm -rf .custom_agents
fi

echo "📁 Creando carpeta .custom_agents vacía..."
mkdir .custom_agents

# 4 y 5: Entrar, clonar y salir
echo "⬇️ Clonando repositorio de skills..."
cd .custom_agents || exit
git clone git@github.com:JVegaB/IA_tools.git --depth=1 .
rm -rf .git
cd ..

# 6, 7 y 8: Revisar, borrar y recrear el archivo .cursorrules
if [ -f ".cursorrules" ]; then
    echo "🗑️ Borrando archivo .cursorrules existente..."
    rm .cursorrules
fi

echo "📄 Creando nuevo .cursorrules vacío..."
touch .cursorrules

# 9: Concatenar el contenido de todos los identity.md en el .cursorrules
echo "🔗 Concatenando identidades en .cursorrules..."

# Verificamos de forma segura si existe al menos un archivo identity.md en los subdirectorios
if ls .custom_agents/*/identity.md 1> /dev/null 2>&1; then
    # Agregamos una cabecera opcional por limpieza
    echo "# ==========================================" >> .cursorrules
    echo "# 🤖 Agentes Locales Inyectados Automáticamente" >> .cursorrules
    echo "# ==========================================" >> .cursorrules
    echo "" >> .cursorrules
    
    # Concatenamos todos los archivos
    cat .custom_agents/*/identity.md >> .cursorrules
    
    echo "✅ Identidades inyectadas exitosamente."
else
    echo "⚠️ No se encontraron archivos identity.md para concatenar."
fi

echo "🎉 Configuración de entorno completada con éxito."