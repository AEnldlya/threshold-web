# Google Drive Upload Process

## Target Folder
https://drive.google.com/drive/folders/1UcB6g9SjAUh7tQQ8YPDxbVwJWBdYKkhf?usp=sharing

## Setup Required (One-time)

1. Get Google OAuth credentials:
   - Go to https://console.cloud.google.com/
   - Create a project (or use existing)
   - Enable Google Drive API
   - Create OAuth 2.0 credentials (Desktop app)
   - Download the `client_secret.json` file

2. Authenticate gog:
   ```bash
   gog auth credentials /path/to/client_secret.json
   gog auth add your-email@gmail.com --services drive
   ```

3. Verify auth:
   ```bash
   gog auth list
   ```

## Upload Commands (Ready to run after auth)

### Today's Boston Call List
```bash
gog drive upload /home/clawdbot/.openclaw/workspace/DAILY_CALL_LIST_2026-03-16.csv \
  --folder "1UcB6g9SjAUh7tQQ8YPDxbVwJWBdYKkhf" \
  --name "MA-Boston-2026-03-16.csv"
```

### Future uploads will follow this pattern:
- Folder structure: One folder per state
- File naming: [STATE]-[CITY]-[DATE].csv
- Example: TX-Austin-2026-03-17.csv

## Files Ready for Upload

| File | State | City | Date |
|------|-------|------|------|
| DAILY_CALL_LIST_2026-03-16.csv | MA | Boston | 2026-03-16 |

## Notes
- Run `gog drive list --folder "FOLDER_ID"` to verify uploads
- Create state subfolders as needed
- Email lists will follow same pattern
