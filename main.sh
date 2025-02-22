#!/bin/bash

# Define colors (dark purple to light pink gradient)
DARK_PURPLE="\033[38;5;55m"  # Dark Purple
PURPLE_2="\033[38;5;93m"     # Slightly lighter purple
PURPLE_3="\033[38;5;141m"    # Mid purple
PURPLE_4="\033[38;5;177m"    # Light purple
PINK_1="\033[38;5;213m"      # Light Pink
PINK_2="\033[38;5;218m"      # Very Light Pink
RESET="\033[0m"              # Reset color

# Define tools directory
TOOLS_DIR="./tools"

# Display Banner with Gradient
echo -e "${DARK_PURPLE}███╗   ██╗ █████╗ ██████╗  ██████╗ ██╗     ██╗ ██╗██████╗ ███████╗██████╗${RESET}"
sleep 0.3
echo -e "${PURPLE_2}████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██║     ██║███║╚════██╗╚════██║╚════██╗${RESET}"
sleep 0.3
echo -e "${PURPLE_3}██╔██╗ ██║███████║██████╔╝██║   ██║██║     ██║╚██║ █████╔╝    ██╔╝ █████╔╝${RESET}"
sleep 0.3
echo -e "${PURPLE_4}██║╚██╗██║██╔══██║██╔═══╝ ██║   ██║██║     ██║ ██║ ╚═══██╗   ██╔╝ ██╔═══╝ ${RESET}"
sleep 0.3
echo -e "${PINK_1}██║ ╚████║██║  ██║██║     ╚██████╔╝███████╗██║ ██║██████╔╝   ██║  ███████╗${RESET}"
sleep 0.3
echo -e "${PINK_2}╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝╚═╝ ╚═╝╚═════╝    ╚═╝  ╚══════╝${RESET}"
sleep 0.5


while true; do
  # Display the menu with the same gradient colors
  echo -e "\n${DARK_PURPLE}#═╦═══════» ${PINK_1}[1] Link Dumper (domain)${RESET}"
  echo -e "${PURPLE_2}╚═╦══════» ${PINK_2}[2] Link Dumper (file)${RESET}"
  echo -e "${PURPLE_3}╚═╦═════» ${PINK_1}[3] help${RESET}"
  echo -e "${PURPLE_4}╚═╦═════» ${PINK_2}[4] Exit${RESET}"
  echo -n -e "${RESET}Choose an option: "
  
  read -r choice

  case "$choice" in
    1)
      # Execute Link dumper (assuming it's in the tools folder)
      if [ -f "$TOOLS_DIR/Link_dumper.py" ]; then
        echo -e "${PURPLE_3}Running Link Dumper Tool...${RESET}"
        python3 "$TOOLS_DIR/Link_dumper.py"
      else
        echo -e "${PINK_2}Tool not found in the folder!${RESET}"
      fi
      ;;
    2)
      # Execute Link dumper V2 (assuming it's in the tools folder)
      if [ -f "$TOOLS_DIR/Link_dumper_v2.py" ]; then
        echo -e "${PURPLE_3}Running Link_dumper_v2 Tool...${RESET}"
        python3 "$TOOLS_DIR/Link_dumper_v2.py"
      else
        echo -e "${PINK_2}Tool not found in the folder!${RESET}"
      fi
      ;;
    3)
      # Execute help (assuming it's in the tools folder)
      if [ -f "$TOOLS_DIR/help.sh" ]; then
        echo -e "${PURPLE_3}Running Bypass Tool...${RESET}"
        bash "$TOOLS_DIR/help.sh"
      else
        echo -e "${PINK_2}Tool not found in the folder!${RESET}"
      fi
      ;;
    4)
      echo -e "${PINK_2}Exiting...${RESET}"
      break
      ;;
    *)
      echo -e "${PINK_2}Invalid choice, please choose again.${RESET}"
      ;;
  esac
done

