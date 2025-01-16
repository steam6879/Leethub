from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Create a dictionary mapping emails to account indices
        email_to_accounts = defaultdict(list)
        visited = [False] * len(accounts)
        merged_accounts = []

        # Step 1: Build mapping of email to account indices
        for account_idx, account in enumerate(accounts):
            # Skip name (index 0) and process only emails
            for email in account[1:]:
                email_to_accounts[email].append(account_idx)

        def find_connected_emails(account_idx: int, connected_emails: set) -> None:
            """
            DFS function to find all connected emails for an account
            Args:
                account_idx: Index of the current account
                connected_emails: Set to store all connected emails
            """
            if visited[account_idx]:
                return

            visited[account_idx] = True
            current_account = accounts[account_idx]
            
            # Process all emails in current account
            for email in current_account[1:]:
                connected_emails.add(email)
                # Check other accounts containing this email
                for linked_account_idx in email_to_accounts[email]:
                    if not visited[linked_account_idx]:
                        find_connected_emails(linked_account_idx, connected_emails)

        # Step 2: Merge accounts using DFS
        for account_idx, account in enumerate(accounts):
            if visited[account_idx]:
                continue

            account_name = account[0]
            connected_emails = set()
            
            # Find all connected emails using DFS
            find_connected_emails(account_idx, connected_emails)
            
            # Add merged account with sorted emails
            merged_accounts.append([account_name] + sorted(connected_emails))

        return merged_accounts