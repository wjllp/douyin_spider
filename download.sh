start=$(date +%s)
i=0
cat urls.txt | (while read line
do
    ((i++))
    echo "正在下载第$i个视频"
    wget -c ${line} -O "video/${i}.mp4"
done
echo "总共下载了$i个视频")
end=$(date +%s)
echo "总共花费了$(( $end - $start ))秒"
