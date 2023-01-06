/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
}

module.exports = {
  async exportPathMap(defaultPathMap) {
    return {
      "/api/data": { page: "/api/data" },
    };
  },
};
