# 📚 Another Way of Learning English Words with Obsidian and Anki
A powerful system to help you memorize and track vocabulary using **Obsidian**, **Anki**, Make it even more powerful by installing **Anki** on mobile and adjust synchronization with **Dropbox** by using **Dropbox sync** **app**, tailored for seamless bilingual learning and spaced repetition. 

---
## Technologies to use 
![[Pasted image 20250525211601.png]]
### ![[obsidian-logo-gradient.svg|25]] Obsidian
After installing Obsidian open this repository as vault
#### Required plugins and their configurations:

-  **Templater**
	- Bind `templates/Anki Template.md` to `Ctrl + Shift + U` via **Settings → Hotkeys**.
	    
-  **Obsidian_to_Anki**
	- Set **Scan Directory** to your `Education` folder.  You can find this configuration under the **Defaults** section of this plugin
	    
-  **Dataview**
	- Enable **JavaScript queries** to allow rendering charts. You can find this switcher in the **Dataview** configurations

- **Charts**
---
### ![[Pasted image 20250525171307.png|25]] Anki

#### Required:

- Install [AnkiConnect](https://ankiweb.net/shared/info/2055492159) via **Tools → Add-ons**.
    
- Anki must be **open** during sync from Obsidian.
    
#### Actions required in Anki: 

- Adjust card fields to match with obsidian template ![[Pasted image 20250525172036.png|500]]

- Set up these card templates for front and back and styling ![[Pasted image 20250525172550.png|500]]

**Front Template**
```html
{{Front}}

<button type="button" class="collapsible">Examples:</button>
<div class="content">
  <p>{{Examples}}</p>
</div>

<script>
var coll = document.getElementsByClassName("collapsible");
for (var i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    content.style.display = content.style.display === "block" ? "none" : "block";
  });
}
</script>
```

**Back Template**
```html
{{FrontSide}}

<hr id="answer">

<div style='font-family: "Arial"; font-size: 20px;'>{{Link to Obsidian}}</div>

{{Back}}
```

**Styling**
```css
.card {
  font-family: arial;
  font-size: 20px;
  text-align: center;
  color: black;
  background-color: white;
}

.collapsible {
  background-color: #c6e2ff;
  color: black;
  cursor: pointer;
  padding: 18px;
  width: 90%;
  border: none;
  text-align: left;
  font-size: 15px;
}

.content {
  padding: 0 18px;
  display: none;
  background-color: #f1f1f1;
}
```
- Register and sign in [AnkiWeb](https://ankiweb.net/about)
---
### ![[Pasted image 20250525202158.png|25]] Dropbox
- Place your **Obsidian vault** inside the `DropsyncFiles` folder in **Dropbox**

---
### Mobile:
- Install Anki for mobile
- Install Obsidian for mobile
-  Install [Dropsync](https://play.google.com/store/apps/details?id=com.ttxapps.dropsync)  for mobile
- 🔄 Sync Setup: Obsidian ↔️ Anki ↔️ Mobile
    - Log into **Dropsync** and sync the `DropsyncFiles` folder from Dropbox.
    - Add **two widgets** to your Android home screen:
        - 📚 AnkiDroid deck access
        - 🔄 "Sync now" button for Dropsync![[Pasted image 20250525203001.png|300]]
            

---

## 📝 How to Create Markdown Files for Anki Cards
![[Another Way of Learning English Words with Obsidian and Anki - visual selection.png]]
### Use Case:

When reading an English article and discovering a new word:

1. On Android, open the Obsidian folder inside the synced Dropbox.
    
2. Create a **new note** with a `!` prefix in the filename (e.g., `!Cat.md`).
    
    - This pins the file to the top of your folder for easy access.![[ezgif-36ada158cb1897.gif]]

### Populate Note with Template:

1. Open the new file (e.g., `!Cat.md`) in Obsidian on your PC.
    
2. Press `Ctrl + Shift + U` to apply the **Templater** Anki template.![[obsidian-sync 1.gif]]
    

### 🐍Enrich Your Note with Content:

- Run the `mp3downloader.py` script:
    
    1. Open the terminal from the `Scripts` folder.
        
    2. Run: `python -i mp3downloader.py`
        
    3. Enter your destination language code (e.g., `tr` for Turkish).
        
    4. Visit [Cambridge Dictionary](https://dictionary.cambridge.org/) and copy the URL of the word you're learning.
        
    5. Paste the URL into the script prompt.
        
    6. The script will insert definitions, examples, and MP3 audio links into the note.
        
- Manually add an image:
    
    1. Search the word on the internet with "word meaning".
        
    2. Copy a suitable image.
        
    3. Paste it into the **Front** section of your markdown file.
        
![[obsidian-sync 2.gif]]
### Final Step - Push your new cards into a Anki deck:

- Open Anki
- Run `Obsidian_to_Anki` in Obsidian.
- Wait until cards are created.
- Hit Sync in Anki
- Sync AnkiDroid on mobile
- Done! Now review your cards on the go
![[obsidian-sync 3.gif]]

---

## ✅ Summary

This setup allows you to:

- Instantly capture vocabulary while reading.
    
- Enrich your notes with examples, images, and audio.
    
- Sync across devices via Dropbox.
    
- Study flashcards in Anki or AnkiDroid anytime.
    
- Use **Alphabet.md** to review your deck in Obsidian
- Use **Chart.md** to see your weekly statistic
- Use **Table.md** to see your words in a table view

---
## For contributors: 
### Maintaining CHANGELOG.md
### 📖 Contributor workflow: 

- Get the latest git repository 
`git checkout develop`
`git pull origin develop`
- Create a branch
`git checkout -b my-new-working-branch-name`
- Do your changes
- Stage your files
`git add .`
-  Commit your changes with a new format if you want your commit be present in a CHANGELOG.md 
`git commit -m "feat(My Developed Tool): my new tool invented"`
- Update your branch with the latest develop changes
`git pull origin develop`
`git merge develop`
- Create pull request
`git push --set-upstream origin my-new-working-branch-name`
OR
If you are in my-new-working-branch-name:
`git push --set-upstream origin HEAD`

**
```
Commit message format:
<type>[optional scope]: <description>

Message example:
feat(New Tool): added a new functionality 

Commit example:
>git commit -m "feat(New Tool): added a new functionality"
```

We will limit types to a specific set:

| Commit <type> | Changelog section name | Note                                                       |
| ------------- | ---------------------- | ---------------------------------------------------------- |
| feat          | Added                  | Features, also this is a indicator of minor version update |
| fix           | Fixed                  | also this is a indicator of patch version update           |
| refactor      | Changed                | for changes in existing functionality                      |


Note: commits with all other type will be filtered out from the CHANGELOG.md

We will be regenerating CHANGELOG.md after each new release by simply running:

`git-chglog -o CHANGELOG.md`

Note: you need to set up [git-chnglog](https://github.com/git-chglog/git-chglog) in your local machine to run the above command.

![[Pasted image 20250525212436.png]]

For more information please follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification

### 📖 Reviewer workflow
- Merge PRs to `develop` branch (on GitHub)
- To create a tag switch to develop branch: 
`git checkout develop`
- Get the latest repository
`git pull origin develop`
- Create a tag on develop branch
`git tag -a version/0.5.6 -m "Release 0.5.6"`
- Push tag to the GitHub
`git push origin version/0.5.6`