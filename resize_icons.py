from PIL import Image
import os

# Chemins des fichiers
source = r"C:\Users\janda\OneDrive\Documentos\sngine_english\assets\icon\app_icon.png"
output_dir = r"C:\Users\janda\deploy-web\icons"

os.makedirs(output_dir, exist_ok=True)

# Ouvrir l'image source
img = Image.open(source).convert("RGBA")

def create_icon(source_img, size, logo_ratio, output_path, bg_color=(46, 125, 50, 255)):
    """
    Crée une icône avec fond coloré et logo centré.
    logo_ratio: proportion de la taille totale occupée par le logo (0.5 = 50%)
    """
    # Créer un canvas carré avec fond coloré
    canvas = Image.new("RGBA", (size, size), bg_color)
    
    # Calculer la taille du logo
    logo_size = int(size * logo_ratio)
    logo = source_img.resize((logo_size, logo_size), Image.LANCZOS)
    
    # Centrer le logo
    offset = (size - logo_size) // 2
    canvas.paste(logo, (offset, offset), logo)
    
    # Sauvegarder
    canvas.save(output_path, "PNG")
    print(f"✅ {output_path}")

# Icônes standard (logo occupe ~70% de l'espace)
create_icon(img, 192, 0.70, os.path.join(output_dir, "Icon-192.png"))
create_icon(img, 512, 0.70, os.path.join(output_dir, "Icon-512.png"))

# Icônes maskable (logo occupe ~45% pour laisser de la marge de sécurité)
create_icon(img, 192, 0.45, os.path.join(output_dir, "Icon-maskable-192.png"))
create_icon(img, 512, 0.45, os.path.join(output_dir, "Icon-maskable-512.png"))

# Favicon
create_icon(img, 64, 0.70, os.path.join(output_dir, "favicon.png"))

print("\n🎉 Toutes les icônes ont été générées !")