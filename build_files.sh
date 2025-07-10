

echo "📦 Installing dependencies..."
python3.9 -m pip install -r requirements.txt

echo "📁 Creating staticfiles directory..."
mkdir -p staticfiles

echo "📁 Applying migrations..."
python3.9 manage.py migrate --run-syncdb

echo "🎨 Collecting static files..."
python3.9 manage.py collectstatic --no-input --clear

echo "✅ Build completed!"