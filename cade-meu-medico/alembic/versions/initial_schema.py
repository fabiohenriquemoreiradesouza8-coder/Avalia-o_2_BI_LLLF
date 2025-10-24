from alembic import op 
import sqlalchemy as sa 
from app.db.models import UserRole # Para importar o Enum 
 
revision = '0001_initial_schema' 
down_revision = None 
branch_labels = None 
depends_on = None 
 
def upgrade(): 
    # Tabela users 
    op.create_table('users', 
    sa.Column('id', sa.Integer(), index=True, nullable=False, primary_key=True), 
    sa.Column('full_name', sa.String(length=100), index=True, nullable=True), 
    sa.Column('email', sa.String(length=100), unique=True, index=True, nullable=False), 
    sa.Column('hashed_password', sa.String(), nullable=False), 
    sa.Column('role', sa.Enum(UserRole), nullable=False, default='user') 
    ) 
 
    # Tabela specialties 
    op.create_table('specialties', 
    sa.Column('id', sa.Integer(), index=True, nullable=False, primary_key=True), 
    sa.Column('name', sa.String(length=100), unique=True, index=True, nullable=False) 
    ) 
 
    # Tabela cities 
    op.create_table('cities', 
    sa.Column('id', sa.Integer(), index=True, nullable=False, primary_key=True), 
    sa.Column('name', sa.String(length=100), nullable=False), 
    sa.Column('state', sa.String(length=2), nullable=False) 
    ) 
 
    # Tabela doctors 
    op.create_table('doctors', 
    sa.Column('id', sa.Integer(), index=True, nullable=False, primary_key=True), 
    sa.Column('name', sa.String(length=100), index=True, nullable=False), 
    sa.Column('crm', sa.String(length=20), unique=True, index=True, nullable=False) 
    ) 
 
    # Tabela doctor_specialties (Many-to-Many) 
    op.create_table('doctor_specialties', 
    sa.Column('doctor_id', sa.Integer(), sa.ForeignKey('doctors.id'), primary_key=True), 
    sa.Column('specialty_id', sa.Integer(), sa.ForeignKey('specialties.id'), primary_key=True) 
    ) 
 
    # Tabela doctor_cities (Many-to-Many) 
    op.create_table('doctor_cities', 
    sa.Column('doctor_id', sa.Integer(), sa.ForeignKey('doctors.id'), primary_key=True), 
    sa.Column('city_id', sa.Integer(), sa.ForeignKey('cities.id'), primary_key=True) 
    ) 
 
def downgrade(): 
    op.drop_table('doctor_cities') 
    op.drop_table('doctor_specialties') 
    op.drop_table('doctors') 
    op.drop_table('cities') 
    op.drop_table('specialties') 
    op.drop_table('users') 
