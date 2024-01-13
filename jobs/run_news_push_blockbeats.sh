


ts=$(date +%s)
if ( ps aux | grep "python news_push_blockbeats.py" | grep grep -v >/dev/null 2>&1 ); then
    echo $ts [$(date)] "Processing ..."
else
    echo $ts [$(date)] "Start ..."
    /home/ubuntu/miniconda3/envs/news-push/bin/python -u news_push_blockbeats.py >>log.python.news_push_blockbeats 2>&1
    echo $ts [$(date)] "End !!!" 
fi

