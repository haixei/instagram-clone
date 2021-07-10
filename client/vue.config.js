// Proxy the calls
module.exports = {
    devServer: {
        proxy: {
            "/api/*": {
                target: "http://server:8000",
            }
        }
    }
};
