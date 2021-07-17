# election-analysis

## Election Audit Overview
The puprose of this project was to audit the results of a congressional election to determine the winner.  We were tasked with determining several criteria points:
    1. Total Number of Votes Cast
    2. Total Number of Votes Cast Based on County
    3. Total Number of Votes Cast for Each Candidate
    4. Winner of the Election
## Resources
We used python version 3.9.6 and vs code version 1.58 to conduct our analysis.  Our data was derived from the election_results.csv file.
## Election Audit Results
Based on our analysis of the election data we concluded the following:

    * The total number of votes cast was 369,711
    * County Breakdown: Denver had the largest voter turnout with 306,055 votes cast
        * Jefferson County: 38,855 votes
        * Denver County: 306,055 votes
        * Arapahoe: 24,801 votes
    * Candidate Breakdown: Diane DeGette had the most votes with 272,892
        * Charles Casper Stockham: 85,213 votes (23.0% of the vote)
        * Diane DeGette: 272,892 votes (73.8% of the vote)
        * Raymon Anthony Doane: 11,606 votes (3.1% of the vote)
    * The Winner of the election was Diane DeGette.
## Election Audit Summary
Our Code demonstrated a reliable way for determining the results of an election.  Further modifications can be made to the code to enhance its capabilites.  One such enchancement would be to create a way to determine the breakdown for the number of votes each candidate recieved by county.  This would allow a user to get a better understanding of which counties favored certain candidates. 

A second enhancement would be to detail voter demographics.  This would require more data then what was provided, but would prove very useful when analyzing the election results.  Some demographics that would be useful to capture would be county population size, voter pary registration, and the way the voter cast their vote.  The code could easily be modified to capture this new data.