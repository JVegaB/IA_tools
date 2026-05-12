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

# 6: Por cada carpeta hija directa, combinar head.yml e identity.md en SKILL.md
echo "📦 Generando archivos SKILL.md por agente..."

for agent_dir in .custom_agents/*/; do
    [ -d "$agent_dir" ] || continue

    head_file="${agent_dir}head.yml"
    identity_file="${agent_dir}identity.md"
    skills_file="${agent_dir}SKILL.md"

    if [ ! -f "$head_file" ] && [ ! -f "$identity_file" ]; then
        echo "⚠️  Saltando ${agent_dir}: no se encontró head.yml ni identity.md"
        continue
    fi

    : > "$skills_file"

    if [ -f "$head_file" ]; then
        cat "$head_file" >> "$skills_file"
        echo "" >> "$skills_file"
    fi

    if [ -f "$identity_file" ]; then
        cat "$identity_file" >> "$skills_file"
    fi

    echo "✅ SKILL.md generado en ${agent_dir}"
done

echo "🎉 Configuración de entorno completada con éxito."
