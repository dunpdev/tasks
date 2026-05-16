#!/bin/bash
# Quick setup verification script for Railway deployment

set -e

echo "========================================"
echo "Django Railway Deployment Verification"
echo "========================================"
echo ""

# Check if Python is installed
echo "Checking Python installation..."
python --version
echo "✓ Python found"
echo ""

# Check if virtual environment is active
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "⚠️  WARNING: Virtual environment not activated"
    echo "   Run: source venv/bin/activate (on Linux/Mac)"
    echo "   Or:  venv\Scripts\activate (on Windows)"
    echo ""
else
    echo "✓ Virtual environment is active"
    echo ""
fi

# Check if requirements are installed
echo "Checking required packages..."
pip list | grep -E "Django|gunicorn|celery|redis|psycopg2" || echo "⚠️  Some packages might be missing"
echo ""

# Check environment file
echo "Checking .env file..."
if [ -f .env ]; then
    echo "✓ .env file exists"
    echo "  Variables set:"
    cat .env | grep -v "^#" | grep -v "^$" | sed 's/^/    - /'
else
    echo "⚠️  .env file not found"
    echo "   Copy from .env.example: cp .env.example .env"
    echo "   Then edit with your settings"
fi
echo ""

# Check Django settings
echo "Checking Django settings..."
python manage.py check 2>&1 | head -20
echo ""

# Show deployment files
echo "Checking deployment files..."
files=("Procfile" "runtime.txt" "requirements.txt" ".env.example" "RAILWAY_DEPLOYMENT.md")
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✓ $file"
    else
        echo "✗ $file (MISSING)"
    fi
done
echo ""

echo "========================================"
echo "Verification complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Review your .env file for correct settings"
echo "2. Run: python manage.py migrate"
echo "3. Run: python manage.py collectstatic --noinput"
echo "4. Read RAILWAY_DEPLOYMENT.md for deployment instructions"
echo ""
