# 091924 Experiment

Experiment: perform a specific set of actions in Resolve and record the associated log entries.

### Test Actions

- **Start App**
  *Timestamp:* 2024-09-19 09:23:01
  *Associated log entry:*
  ```plaintext
  0x2039ccf40    | Undefined            | INFO  | 2024-09-19 09:23:06,403 | --------------------------------------------------------------------------------
  0x2039ccf40    | Undefined            | INFO  | 2024-09-19 09:23:06,404 | Loaded log config from /Users/granthall/Library/Preferences/Blackmagic Design/DaVinci Resolve/log-conf.xml
  0x2039ccf40    | Undefined            | INFO  | 2024-09-19 09:23:06,404 | --------------------------------------------------------------------------------
  ```

- **Open and Close "Finished" Folder in project manager**
  *Performed after:* 2024-09-19 09:23:44
  *Associated log entry:* none

- **Open -CHOP-**
  *Performed after:* 2024-09-19 09:24:01
  *Associated log entry:*
  ```plaintext
  0x2039ccf40    | SyManager.ActionExecutor | INFO  | 2024-09-19 09:24:08,241 | Database transaction is ongoing, user initiated action Sync Asset Map is postponed
  0x2039ccf40    | SyManager.ActionExecutor | INFO  | 2024-09-19 09:24:08,517 | Database transaction completed, enqueueing 1 postponed actions
  0x2039ccf40    | SyManager.ProjectManager | INFO  | 2024-09-19 09:24:09,113 | Loading project (-CHOP-) from project library (Local Database) took 1817 ms
  ```

- **Switch to ^1,2,3,4,5,6,7,8**
  *Performed after:* 2024-09-19 09:25:22
  *Associated log entry:*
  ```plaintext
  0x2039ccf40    | SyManager.Signals    | INFO  | 2024-09-19 09:25:28,475 | Main view page is changed to 12
  ```

- **Switch Back to Edit**
  *Performed after:* 2024-09-19 09:26:28
  *Associated log entry:*
  ```plaintext
  0x2039ccf40    | SyManager.Signals    | INFO  | 2024-09-19 09:26:34,082 | Main view page is changed to 2
  ```

- **Make a New Timeline and Drag Files In**
  *Performed after:* 2024-09-19 09:26:52
  *Associated log entry:*
  ```plaintext
  0x2039ccf40    | SyManager.Signals    | INFO  | 2024-09-19 09:27:11,173 | Current timeline pointer (tmp-timline) is changed
  ```

- **Change Some Project Setting**
  *Performed after:* 2024-09-19 09:28:14
  *Associated log entry:* none

- **Change Some User Preference**
  *Performed after:* 2024-09-19 09:29:03
  *Associated log entry:* none

- **Render Audio File**
  *Performed just before:* 2024-09-19 09:31:15
  *Associated log entry:*
  ```plaintext
  0x311c43000    | GsManager            | INFO  | 2024-09-19 09:30:51,022 | Finished recording 25 frames.
  ```

- **Start Wait 30 Min**
  *Performed after:* 2024-09-19 09:31:26
  *Associated log entry:*
  ```plaintext
  0x2039ccf40    | SyManager.AutoSave   | INFO  | 2024-09-19 09:44:12,957 | Start autosave
  0x2039ccf40    | SyManager.AutoSave   | INFO  | 2024-09-19 09:44:12,957 | Auto saving current project <-CHOP->
  0x2039ccf40    | SyManager.AutoSave   | INFO  | 2024-09-19 09:44:12,957 | Creates an autosave copy for current project in database
  0x2039ccf40    | SyManager.Gallery    | INFO  | 2024-09-19 09:44:12,958 | Started loading 2 stills into the cache
  0x2039ccf40    | SyManager.Gallery    | INFO  | 2024-09-19 09:44:12,967 | Finished loading 2 still objects into the cache
  0x2039ccf40    | SyManager.AutoSave   | ERROR | 2024-09-19 09:44:12,968 | DaVinci Resolve failed to backup -CHOP- as a backup folder could not be created in the selected Project Backup Location.
  0x2039ccf40    | SyManager.ActionExecutor | WARN  | 2024-09-19 09:44:12,968 | Failed to perform action <AutoSaveAction>:
  0x2039ccf40    | BtCommon             | INFO  | 2024-09-19 10:01:24,384 | Exiting sleep mode
  ```

- **Create a New Timeline and Drag a Clip onto It**
  *Performed after:* 2024-09-19 10:01:39
  *Associated log entry:*
  ```plaintext
  0x2039ccf40    | SyManager.Signals    | INFO  | 2024-09-19 10:01:49,305 | Current timeline mode is changed
  0x2039ccf40    | SyManager.Signals    | INFO  | 2024-09-19 10:01:49,340 | Main view page is changed to 2
  0x2039ccf40    | UI                   | ERROR | 2024-09-19 10:02:07,013 | Failed to find text '2160 x 2160 Ultra HD Square' in combo-box
  0x2039ccf40    | SyManager.Signals    | INFO  | 2024-09-19 10:02:09,835 | Current timeline pointer (tmp-timeline2) is changed
  ```

- **Close App**
  *Performed after:* 2024-09-19 10:02:32
  *Associated log entry:*
  ```plaintext
  0x2039ccf40    | SyManager.Project    | INFO  | 2024-09-19 10:02:36,677 | Unlock project -CHOP-
  [...]
  0x2039ccf40    | Main                 | INFO  | 2024-09-19 10:02:37,358 | Starting terminate sequence by calling g_MainTerm
  [...]
  0x2039ccf40    | Main                 | INFO  | 2024-09-19 10:02:37,915 | Main thread exited successfully
  ```

- **Reopen App**
  *Performed after:* 2024-09-19 10:02:50
  *Associated log entry:*
  ```plaintext
  0x2039ccf40    | Undefined            | INFO  | 2024-09-19 10:02:53,862 | --------------------------------------------------------------------------------
  0x2039ccf40    | Undefined            | INFO  | 2024-09-19 10:02:53,862 | Loaded log config from /Users/granthall/Library/Preferences/Blackmagic Design/DaVinci Resolve/log-conf.xml
  0x2039ccf40    | Undefined            | INFO  | 2024-09-19 10:02:53,862 | --------------------------------------------------------------------------------
  ```

- **Close App Again**
  *Performed after:* 2024-09-19 10:03:09
  *Associated log entry:*
  ```plaintext
  0x2039ccf40    | Main                 | INFO  | 2024-09-19 10:03:11,768 | Starting terminate sequence by calling g_MainTerm
  [...]
  0x2039ccf40    | Main                 | INFO  | 2024-09-19 10:03:12,373 | Main thread exited successfully
  ```
