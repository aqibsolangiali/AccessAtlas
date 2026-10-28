# Publish AccessAtlas to the existing GitHub repository

Target repository: https://github.com/aqibsolangiali/AccessAtlas

## Option 1: Upload through GitHub's website

1. Open the existing repository and select **Add file → Upload files**.
2. Extract `AccessAtlas_GitHub_Ready.zip` on your computer first.
3. Upload the *contents* of the `AccessAtlas_GitHub` folder (not the outer folder itself). Include hidden files such as `.gitignore` and `.github/workflows/tests.yml`.
4. If GitHub says `README.md`, `app.py`, or other files already exist, review the differences before replacing them. Do not overwrite existing work you want to keep.
5. Add a commit message such as `Add AccessAtlas dashboard project files` and commit the changes.

## Option 2: Push with Git

If you are comfortable using Git, clone the existing repository first so you preserve its current history:

```bash
git clone https://github.com/aqibsolangiali/AccessAtlas.git
cd AccessAtlas
```

Copy the contents of the extracted `AccessAtlas_GitHub` folder into the cloned repository. Review any files that would be overwritten, then run:

```bash
git add .
git status
git commit -m "Add AccessAtlas dashboard project files"
git push
```

If the repository is not empty, resolve any conflicts carefully rather than force-pushing.

## Optional: Deploy the dashboard

After the app files are committed, you can deploy through Streamlit Community Cloud at https://share.streamlit.io/. Choose the `aqibsolangiali/AccessAtlas` repository, branch `main`, and `app.py` as the app entrypoint. Check the app and repository settings before publishing.

**Privacy reminder:** The included sample CSV is synthetic. Do not commit real student-identifying data or secrets.
