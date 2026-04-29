 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/README.md b/README.md
new file mode 100644
index 0000000000000000000000000000000000000000..55a7f0880d857ab76d1bc782fb175fdca99d8776
--- /dev/null
+++ b/README.md
@@ -0,0 +1,58 @@
+# GSM X Maroc
+
+Landing pages for **UnlockTool Maroc** and related GSM services in Morocco. This repository contains static HTML pages used for publishing service information, offers, and customer contact channels.
+
+## Live website
+
+You can view the live project here:
+
+- https://gsm-x-morocco-two.vercel.app/
+
+## What this project includes
+
+- `index.html`: Main homepage for UnlockTool Maroc.
+- `unlocktool.html`: Dedicated page for UnlockTool services.
+- `iptv.html`: IPTV-focused service page.
+- `borneo.html`: Borneo tool/service information page.
+- Image assets (`.png`, `.jpg`) used by the pages.
+
+## Main services presented
+
+- Mobile phone unlock and software support.
+- IPTV subscription information.
+- GSM tool-related service pages for Moroccan customers.
+
+## Tech stack
+
+- Pure **HTML/CSS** (static website)
+- No backend framework
+- No build step required
+
+## How to see the project
+
+###    ----- Visit the live website
+
+- https://gsm-x-morocco-two.vercel.app/
+

+## Contact
+
+Business contact details are listed directly on the website pages.
 
EOF
)
