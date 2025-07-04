
echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "📁 Applying migrations..."
python3.11 manage.py migrate

echo "🎨 Collecting static files..."
python3.11 manage.py collectstatic --no-input --clear

echo "✅ Build completed!"
