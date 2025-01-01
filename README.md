# SciCat Bot for Matrix Chatroom 🤖💬  

This repository provides a **SciCat bot** for the **Riot Matrix** chatroom framework. It automates the posting of results from neutron data at the **European Spallation Source (ESS)** to scientists' chatrooms, enabling streamlined communication and collaboration.

---

## Features ✨  

- **Automated Posting**: Shares results from SciCat to Matrix chatrooms.  
- **ESS Integration**: Designed for neutron data workflows.  
- **Riot Matrix Framework**: Utilizes the Matrix protocol for chat-based collaboration.  

---

## Prerequisites 🛠️  

- Node.js (14+ recommended)  
- Access to a Matrix server and SciCat instance  

Install required packages:  
npm install matrix-bot-sdk axios  

---

## Installation  

1. Clone the repository:  
   git clone https://github.com/your-username/scicat-matrix-bot.git  
   cd scicat-matrix-bot  

2. Install dependencies:  
   npm install  

3. Configure the bot:  
   Update `config.json` with Matrix server details, bot credentials, and SciCat API URL.  

4. Start the bot:  
   npm start  

---

## Usage 🔧  

1. **Configure Matrix and SciCat**:  
   - Add the bot to the desired chatroom.  
   - Ensure SciCat API credentials are correctly set in `config.json`.  

2. **Post Results**:  
   - The bot automatically posts new data or updates from SciCat.  

---

## File Structure 📂  

- `bot.js`: Main bot script for handling Matrix interactions.  
- `config.json`: Configuration for Matrix and SciCat integration.  
- `package.json`: Project dependencies and scripts.  
- `README.md`: Documentation for the repository.  

---

## Example Commands  

- Start the bot:  
  npm start  

- Check logs:  
  cat logs/bot.log  

---

## Contributing 🤝  

1. Fork the repository.  
2. Create a new branch:  
   git checkout -b feature/your-feature  

3. Commit your changes:  
   git commit -m "Add your feature"  

4. Push the branch:  
   git push origin feature/your-feature  

5. Open a pull request.  

---

## License 📝  

This project is licensed under the MIT License. See the LICENSE file for details.  

---

**Enhance collaboration with the SciCat Matrix Bot for neutron data!** 🤖💬  
