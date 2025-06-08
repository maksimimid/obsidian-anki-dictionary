import os
import requests
from bs4 import BeautifulSoup
from translate import Translator
# Paths
SCRIPT_DIR = r"."
DOWNLOAD_DIR = os.path.join(SCRIPT_DIR, "downloads")
MD_DIR = r"..\English Vocabulary"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def translate_to(word, translation_code):
    translator = Translator(to_lang=translation_code)
    try:
        translated = translator.translate(word)
        return translated.capitalize()
    except Exception as e:
        print(f"❌ Translation failed: {e}")
        return ''


def download_mp3_and_update_md(url, translation_code):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch page.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    word = url.split('/')[-1].split('?')[0].lower()

    # Download MP3
    audio_tag = soup.find('source', {'type': 'audio/mpeg'})
    if not audio_tag:
        print("MP3 not found.")
        return

    mp3_url = audio_tag.get('src')
    if not mp3_url.startswith("https:"):
        mp3_url = "https:" +'//dictionary.cambridge.org/'+ mp3_url

    mp3_path = os.path.join(DOWNLOAD_DIR, f"{word}.mp3")
    if not os.path.exists(mp3_path):
        audio_data = requests.get(mp3_url, headers=headers).content
        with open(mp3_path, 'wb') as f:
            f.write(audio_data)
        print(f"MP3 saved to {mp3_path}")
    else:
        print(f"MP3 already exists: {mp3_path}")

    # Get IPA spelling
    ipa_tag = soup.find('span', class_='ipa')
    spelling = ipa_tag.text.strip() if ipa_tag else ''

    # Get definition as "example"
    # definition_tags = soup.find_all('div', class_='def ddef_d db')
    definition_tags = soup.find_all('div', class_='def-block ddef_block')

    if len(definition_tags) > 0 :
        examples = "\n".join("- " + tag.text.strip() for tag in definition_tags[0] if not tag.text.strip().find('Add to word list') > -1  and tag.text.strip())
    else:
        examples = ''

    # Translate to
    translation = translate_to(word, translation_code)


    # Markdown path
    md_path = os.path.join(MD_DIR, f"{word.capitalize()}.md")
    if not os.path.exists(md_path):
        print(f"Markdown file not found: {md_path}")
        return

    # Update Markdown
    with open(md_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    audio_link = f"![[{word}.mp3]]"
    inserted_audio_top = False
    inserted_audio_bottom = False
    replaced_spelling = False
    replaced_translation = False
    replaced_examples = False

    for line in lines:
        # Replace Translation
        if line.strip().startswith("translation:") and not replaced_translation:
            line = f"translation: {translation}\n"
            replaced_translation = True
        # Replace spelling
        if line.strip().startswith("spelling:") and not replaced_spelling:
            line = f"spelling: /{spelling}/\n"
            replaced_spelling = True

        # Replace examples
        if line.strip().startswith("Examples:") and not replaced_examples:
            new_lines.append("Examples:\n")
            new_lines.append(examples + "\n")
            replaced_examples = True
            continue  # Skip original "Examples:" line

        new_lines.append(line)

        # Insert audio at bottom
        if not inserted_audio_bottom and line.strip() == "Back:":
            new_lines.append(f"{translation}\n")
            new_lines.append(audio_link + "\n")
            inserted_audio_bottom = True

    with open(md_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

    print(f"Updated markdown: {md_path}")

if __name__ == "__main__":

    translation_code = input("Enter the language to translate to (e.g., 'uk' for Ukrainian, 'tr' for Turkish):").strip()

    while True:
        try:
            url = input("Paste Cambridge Dictionary URL (or type 'exit'): ").strip()
            if url.lower() == 'exit':
                break
            download_mp3_and_update_md(url, translation_code)
        except KeyboardInterrupt:
            print("\nExiting.")
            break
