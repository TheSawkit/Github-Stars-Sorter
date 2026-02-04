"""
Configuration et dictionnaire de mots-clés pour le GitHub Stars Sorter.
"""

# Constantes API
API_BASE_URL = "https://api.github.com"
REPOS_PER_PAGE = 100
API_RATE_LIMIT_DELAY = 0.5

# Paramètres du système de tri
SCORE = {
    "NAME_MATCH": 3,
    "TOPIC_MATCH": 2,
    "GENERAL_MATCH": 1
}

# Fichiers de sortie
OUTPUT_DIR = "exports"
JSON_FILENAME = "mes_stars_github_triees.json"
MD_FILENAME = "README.md"

# Mapping des catégories et de leurs mots-clés
CATEGORIES = {
    "Languages & Frameworks": [
        "python", "javascript", "typescript", "rust", "go", "c++", "java",
        "php", "ruby", "swift", "kotlin", "django", "flask", "fastapi",
        "react", "nextjs", "vue", "angular", "svelte", "node", "framework"
    ],
    "I.A & Data Science": [
        "ai", "machine-learning", "deep-learning", "neural-network", "gpt",
        "llm", "openai", "pytorch", "tensorflow", "data-science", "nlp",
        "vision", "model", "training"
    ],
    "DevOps & Cloud": [
        "docker", "kubernetes", "k8s", "aws", "azure", "gcp", "cloud",
        "serverless", "terraform", "ansible", "ci/cd", "deployment",
        "container", "monitoring", "prometheus", "grafana"
    ],
    "Security & Privacy": [
        "security", "hacking", "pentest", "exploit", "vulnerability",
        "privacy", "encryption", "tor", "vpn", "anonymous", "auth",
        "oauth", "cybersecurity"
    ],
    "Web Tools & Design": [
        "css", "html", "tailwind", "bootstrap", "sass", "design", "ui",
        "ux", "frontend", "web", "browser", "extension", "chrome",
        "firefox", "svg", "icon", "font"
    ],
    "Systems & OS": [
        "linux", "windows", "macos", "android", "ios", "unix", "kernel",
        "os", "operating-system", "shell", "bash", "terminal", "powershell",
        "wsl", "arch", "ubuntu", "debian"
    ],
    "Hardware & IoT": [
        "raspberry", "arduino", "iot", "embedded", "firmware", "hardware",
        "esp32", "stm32", "robotics", "electronics"
    ],
    "Networking": [
        "network", "protocol", "http", "tcp", "udp", "dns", "wifi", "proxy",
        "vpn", "socket", "webrtc", "api", "rest", "graphql", "grpc"
    ],
    "Gaming & Media": [
        "game", "gaming", "unity", "unreal", "godot", "engine", "graphics",
        "opengl", "vulkan", "audio", "video", "ffmpeg", "streaming",
        "music", "sound"
    ],
    "Education & Guides": [
        "tutorial", "guide", "learning", "course", "book", "resource",
        "list", "awesome", "interview", "roadmap", "cheatsheet", "example",
        "demo", "starter", "template"
    ],
    "Tools & Utilities": [
        "tool", "utility", "cli", "productivity", "automation", "script",
        "bot", "editor", "ide", "vscode", "vim", "emacs", "plugin",
        "package", "library"
    ]
}
