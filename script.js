async function searchVideos() {
    const query = document.getElementById('searchQuery').value;
    const url = `https://yewtu.be/api/v1/search?q=${encodeURIComponent(query)}&page=1`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        // 検索結果を表示
        const videoResults = document.getElementById('videoResults');
        videoResults.innerHTML = ''; // 以前の結果をクリア

        data.forEach(video => {
            const videoElement = document.createElement('div');
            videoElement.innerHTML = `
                <h3>${video.title}</h3>
                <p>著者: ${video.author}</p>
                <button onclick="playVideo('${video.videoId}')">再生</button>
            `;
            videoResults.appendChild(videoElement);
        });
    } catch (error) {
        console.error('検索中にエラーが発生しました', error);
    }
}

async function playVideo(videoId) {
    const url = `https://yewtu.be/api/v1/videos/${videoId}`;
    
    try {
        const response = await fetch(url);
        const video = await response.json();
        
        const audioUrl = video.audioStreams[0].url; // 音声ストリームURL（最初のものを選択）
        
        const audioElement = new Audio(audioUrl);
        audioElement.play();
    } catch (error) {
        console.error('動画の再生中にエラーが発生しました', error);
    }
}
