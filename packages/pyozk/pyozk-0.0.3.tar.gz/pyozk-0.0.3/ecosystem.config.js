module.exports = {
  apps: [
    {
      name: "timekeeper",
      script: "app.py",
      interpreter: "./env/bin/python3", // Path to Python interpreter in the virtual environment
      autorestart: true,
      watch: false,
    },
    {
      name: "live_capture_1",
      script: "./live_capture/device_one.py",
      interpreter: "./env/bin/python3", // Path to Python interpreter in the virtual environment
      autorestart: true,
      watch: false,
    },
   {
      name: "live_capture_2",
      script: "./live_capture/device_two.py",
      interpreter: "./env/bin/python3", // Path to Python interpreter in the virtual environment
      autorestart: true,
      watch: false,
    },
  ]
};