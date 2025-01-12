# Resume Scraper

An automated tool to scrape and filter resumes from hiring platforms, currently supporting Unstop (formerly Dare2Compete).

## 🎯 Purpose

This tool helps recruiters and hiring managers automate the process of:
- Downloading resumes from hiring platforms
- Filtering candidates based on customizable criteria
- Reducing manual effort in initial resume screening

## ✨ Features

- **Platform Support**
  - Unstop (formerly Dare2Compete)

- **Automated Scraping**
  - Bulk resume downloads

- **Smart Filtering**
  - Filter by education criteria
  - Experience-based filtering
  - Skills matching
  - Custom filter rules support

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Chrome browser
- Required Python packages (see requirements.txt)

### Installation
#### Clone the repository
git clone https://github.com/yourusername/resume-scraper
#### Navigate to project directory
cd resume-scraper
#### Create Virtual environment
python -m venv venv
#### Activate Virtual environment
source venv/bin/activate
#### Install dependencies
pip install -e .
#### Ensure that you are logged into the unstop account in chrome using the same profile mentioned in the config.py file
#### Basic usage
python3 python-scraper.py --job-url <job_url>

## 🛠️ Technical Details

- Built with Python and Selenium
- Modular design for easy platform additions
- Supports rule based and LLM OpenAI based filtering

## 🗺️ Roadmap

- [ ] Support for more platforms (Linkedin, Indeed, etc.)
- [ ] AI-powered resume ranking
- [ ] Export to ATS-friendly formats
- [ ] GUI interface
- [ ] Resume parsing and standardization

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational purposes only. Please ensure you have permission to scrape data from the platforms you target and comply with their terms of service and robots.txt policies.

## 🙏 Acknowledgments
- Inspired by the need to streamline hiring processes
- Built with respect for platform policies and rate limits

## 📧 Contact

[@thehellmaker](https://twitter.com/thehellmaker)

Project Link: [https://github.com/thehellmaker/resume-scraper](https://github.com/thehellmaker/resume-scraper)
