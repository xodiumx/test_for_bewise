"""add_quiz_model

Revision ID: f70de72c56b0
Revises: 
Create Date: 2023-05-16 12:31:10.526791

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'f70de72c56b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quiz',
                    sa.Column('pk', sa.Integer(), nullable=False),
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('question', sa.String(
                        length=512), nullable=False),
                    sa.Column('answer', sa.String(length=512), nullable=False),
                    sa.Column('created_at', sa.Date(), nullable=False),
                    sa.PrimaryKeyConstraint('pk'),
                    sa.UniqueConstraint('id')
                    )
    op.create_index(op.f('ix_quiz_answer'), 'quiz', ['answer'], unique=False)
    op.create_index(op.f('ix_quiz_created_at'), 'quiz',
                    ['created_at'], unique=False)
    op.create_index(op.f('ix_quiz_question'), 'quiz',
                    ['question'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_quiz_question'), table_name='quiz')
    op.drop_index(op.f('ix_quiz_created_at'), table_name='quiz')
    op.drop_index(op.f('ix_quiz_answer'), table_name='quiz')
    op.drop_table('quiz')
    # ### end Alembic commands ###
